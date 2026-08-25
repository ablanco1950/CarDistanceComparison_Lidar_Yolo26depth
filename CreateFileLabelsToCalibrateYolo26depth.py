"""

Creación del arbol de ficheros para calibrar depth26depth

"""

import os

# Carpetas de destino estructuradas para el dataset de calibración
DIR_DEST_VAL_IMG = "dataset_calibracion/val/images"
DIR_DEST_VAL_DEP = "dataset_calibracion/val/depth"

# Límitar a 100 imágenes para una calibración rápida
#MAX_IMAGENES_CALIBRACION = 100

# Crear la estructura de carpetas si no existe
os.makedirs(DIR_DEST_VAL_IMG, exist_ok=True)
os.makedirs(DIR_DEST_VAL_DEP, exist_ok=True)

opcion="yolo26depth"

import cv2
import numpy as np
import pykitti
from ultralytics import YOLO


# 1. Configura las rutas a los datos descargados de KITTI

basedir=""

date = '2011_09_26'

drive = '0013_extract'  # Cambia por el número de toma que descargues

# 2. Cargar los datos usando pykitti
# Esto lee automáticamente los archivos de calibración y sincronización
data = pykitti.raw(basedir, date, drive)


# Cargamos el modelo YOLO (se descargará automáticamente el modelo preentrenado en COCO)

model = YOLO('yolo26n.pt')
model_depth = YOLO("yolo26n-depth.pt")

# ID de la clase 'car' (coche) en el dataset COCO usado por YOLO
CAR_CLASS_ID = 2 


ContFrame=0
TotalDife=0

for frame_idx in range(len(data)):
    NameTxt=str(frame_idx)
    while len(NameTxt) < 9:
        NameTxt="0" + NameTxt
    NamePng=NameTxt + ".png"
    NameNpy=NameTxt + ".npy"
    NameTxt=NameTxt + ".txt"
    
    SwHay=0
    #print(NameTxt)
    
    image_pil = data.get_cam2(frame_idx)
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

    h, w, _ = image.shape
    
    # Crear un mapa de profundidad base en blanco (relleno de ceros = sin datos)
    depth_map = np.zeros((h, w), dtype=np.float32)
    
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
            SwHay=1
            # Usamos el percentil 10 o la mediana para evitar ruido o "puntos fantasma" 
            # que atraviesen los cristales del coche y den distancias erróneas
            distancia_lidar = np.percentile(distances_in_box, 20)
            
            
            # caso de querer llevar control con un archivo txt
            #lineaw=[]
            #lineaw.append(str(xmin))
            #lineaw.append(str(ymin))            
            #lineaw.append(str(xmax))
            #lineaw.append(str(ymax))
            #lineaw.append(str(distancia_lidar))            
            #lineaWrite =' '.join(lineaw)
            #lineaWrite=lineaWrite + "\n"            
             
            #with open("dataset_calibracion/val/depth/"+NameTxt, "w", encoding="utf-8") as archivo:
            #    archivo.write(lineaWrite)
                        
            depth_map[ymin:ymax, xmin:xmax] = distancia_lidar            

    
    if  SwHay != 0:    
            cv2.imwrite("dataset_calibracion/val/images/"+ NamePng,image)
            npy_path = os.path.join(DIR_DEST_VAL_DEP, NameNpy)
            np.save(npy_path, depth_map)
              

  
