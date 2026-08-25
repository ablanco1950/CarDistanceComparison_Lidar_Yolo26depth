from ultralytics import YOLO

model = YOLO("yolo26n-depth.pt")
model.calibrate(data="dataset_calibracion/dataset.yaml")
model.save("yolo26n-depth-calibrated.pt")
