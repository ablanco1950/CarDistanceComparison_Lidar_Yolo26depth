"""

Sugerido por la  la IA de google

Para integrar un detector de objetos como YOLO (usando la librería de ultralytics) y
extraer las distancias de los datos del LiDAR de cada imagen del dataset de de KITTI

    1. Detectar los coches en la imagen 2D para obtener sus cajas de delimitación (Bounding Boxes).
    2. Filtrar los puntos del LiDAR que caen exclusivamente dentro de esa caja 2D.
    3. Calcular la distancia promediando la coordenada de profundidad (X en el sistema LiDAR de KITTI) de esos puntos filtrados.
    4. obtener la distancia mediante el sistema yolo26depth y comparar con las distancias proporcionada por el Lidar en el dataset KITTi
    

💻 Instalación de dependencias

pip install ultralytics pykitti opencv-python numpy

🐍 Script: YOLO + KITTI LiDAR para Distancia Automática
Este script procesa un fotograma, detecta los vehículos y calcula su distancia exacta en metros,
dibujando el resultado sobre el propio vídeo. [1]

"""

#opcion="monocular"
opcion="yolo26depth"

import cv2
import numpy as np
import pykitti
from ultralytics import YOLO

# Ancho real promedio de un coche en metros
ANCHO_REAL_COCHE = 1.8  

# Distancia focal de tu cámara en píxeles (f = (Ancho_en_pixeles * Distancia_real) / Ancho_real)
# Si no la conoces, una aproximación estándar para webcams/dashcams comunes es ~700
FOCAL_LENGTH_PX=830.0

def calcular_distancia_monocular(ancho_en_pixeles):
    """
    Aplica el principio de semejanza de triángulos de la cámara estenopeica.
    A partir de  Distancia/Ancho Real = Distancia Focal / Ancho en Píxeles
    Fórmula fundamental: Distancia = (Ancho Real * Distancia Focal) / Ancho en Píxeles
    """
    #if ancho_en_pixeles == 0:
    #    return 0.0
    distancia_metros = (ANCHO_REAL_COCHE * FOCAL_LENGTH_PX) / ancho_en_pixeles
    return distancia_metros

# 1. Configura las rutas a los datos descargados de KITTI

basedir=""

date = '2011_09_26'

drive = '0013_extract'  # Cambia por el número de toma que descargues

# 2. Cargar los datos usando pykitti
# Esto lee automáticamente los archivos de calibración y sincronización
data = pykitti.raw(basedir, date, drive)


# Cargamos el modelo YOLO (se descargará automáticamente el modelo preentrenado en COCO)
#model = YOLO('yolov8n.pt')
model = YOLO('yolo26n.pt')
#model_depth = YOLO("yolo26n-depth.pt")
model_depth=YOLO("yolo26n-depth-calibrated.pt")

# ID de la clase 'car' (coche) en el dataset COCO usado por YOLO
CAR_CLASS_ID = 2 


ContFrame=0
TotalDife=0

for frame_idx in range(len(data)):

    image_pil = data.get_cam2(frame_idx)
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    velo_points = data.get_velo(frame_idx)

    # 3. Matrices de calibración de KITTI
    T_cam2_velo = data.calib.T_cam2_velo
    P_rect_20 = data.calib.P_rect_20

    # 4. Proyectar TODO el LiDAR a 2D para poder indexarlo con las cajas de YOLO
    # Filtramos puntos frente al vehículo (X > 0)
    velo_filtered = velo_points[velo_points[:, 0] > 0]
    pts_3d = velo_filtered[:, :3]
    pts_3d_hom = np.hstack((pts_3d, np.ones((pts_3d.shape[0], 1))))

    # Transformación a cámara y proyección a plano de imagen 2D
    pts_cam = np.dot(T_cam2_velo, pts_3d_hom.T)
    pts_img_hom = np.dot(P_rect_20, pts_cam)
    pts_img = pts_img_hom[:2, :] / pts_img_hom[2, :]

    # 5. Ejecutar detección con YOLO en el fotograma
    results = model(image, verbose=False)[0]

    #  Obtener el mapa de profundidad monocular (en metros)
    resultado_depth = model_depth(image,verbose=False) #MOD
    # El mapa de profundidad viene en formato tensor flotante alineado a la imagen
    mapa_profundidad = resultado_depth[0].depth.data.cpu().numpy().squeeze() 

    # 6. Analizar las detecciones de YOLO y cruzar con LiDAR
    for box in results.boxes:
        # Filtrar para procesar únicamente coches
        if int(box.cls[0]) != CAR_CLASS_ID:
            continue
            
        # Obtener coordenadas de la caja 2D [xmin, ymin, xmax, ymax]
        xmin, ymin, xmax, ymax = map(int, box.xyxy[0].cpu().numpy())
        conf = float(box.conf[0])

        if conf < 0.8: continue
        
        # Buscar qué puntos proyectados del LiDAR caen DENTRO de esta caja de YOLO
        # pts_img[0, :] son las X en píxeles, pts_img[1, :] son las Y en píxeles
        mask_in_box = (
            (pts_img[0, :] >= xmin) & (pts_img[0, :] <= xmax) &
            (pts_img[1, :] >= ymin) & (pts_img[1, :] <= ymax)
        )
        
        # Extraer las distancias reales (X del LiDAR) de esos puntos específicos
        distances_in_box = pts_3d[mask_in_box, 0]
        
        if len(distances_in_box) > 0:
            # Usamos el percentil 10 o la mediana para evitar ruido o "puntos fantasma" 
            # que atraviesen los cristales del coche y den distancias erróneas
            distancia_lidar = np.percentile(distances_in_box, 20)
            
            # 7. Dibujar los resultados en la imagen
            # Caja de YOLO
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

            if opcion=="monocular":
               ancho_caja = xmax - xmin
               distancia_vision =calcular_distancia_monocular(ancho_caja)


               
            else:
                
                # Definir una región central dentro del coche para evitar el fondo exterior
                ancho_caja = xmax - xmin
                alto_caja = ymax - ymin
                cx1 = int(xmin + ancho_caja * 0.3)
                cx2 = int(xmin + ancho_caja * 0.7)
                cy1 = int(ymin + alto_caja * 0.3)
                cy2 = int(ymin + alto_caja * 0.7)
                
                # Recortar la zona del mapa de profundidad correspondiente al coche
                zona_coche_depth = mapa_profundidad[cy1:cy2, cx1:cx2]
                
                # Calcular la distancia mediana (más robusta que el promedio ante ruidos)
                distancia_vision = np.median(zona_coche_depth)
            
            # Etiqueta con la distancia calculada en metros
            #label = f"Coche: {distancia_estimada:.2f}m (Conf: {conf:.2f})"
            #label = f"lidar: {distancia_lidar:.2f}m  vision: {distancia_vision:.2f}m "
            label1 = f"{distancia_lidar:.2f}m "
            label2 = f"{distancia_vision:.2f}m "

            Dife=distancia_lidar - distancia_vision
            if Dife < 0: Dife=Dife*(-1)

            ContFrame=ContFrame +1 
            TotalDife=TotalDife + Dife
            MediaDife= TotalDife/ContFrame
            

            cadena = f"Distance acording Lidar: {distancia_lidar:.2f}m Distance according vision: {distancia_vision:.2f}m"
            cadena = cadena + f" TotalDife :{TotalDife:.2f}m Media :{MediaDife:.2f}m"
            print(cadena)
            
            cv2.putText(image, label1, (xmin, ymin - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 0), 1)
            cv2.putText(image, label2, (xmin+70, ymin - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            """
            # Opcional: Dibujar los puntos de LiDAR que pertenecen a este coche
            puntos_coche = pts_img[:, mask_in_box]
            for p in range(puntos_coche.shape[1]):
                px, py = int(puntos_coche[0, p]), int(puntos_coche[1, p])
                cv2.circle(image, (px, py), 1, (255, 0, 0), -1)
            """    

    # 8. Mostrar el fotograma final procesado
    cv2.imshow("Deteccion Automatica de Distancia con YOLO + LiDAR", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
