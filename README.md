# CarDistanceComparison_Lidar_Yolo26deph
Performs a comparison between distance data returned by a lidar stored in KITTI (https://www.cvlibs.net/datasets/kitti/raw_data.php), dataset 2011_09_26_drive_0013, with car distance estimates from yolo26depth over the frames accompanying the lidar estimates.

Requirements:

pip install ultralytics pykitti opencv-python numpy

It is important to have the latest version of ultralytics; otherwise, the recently created yolo26 module may not be found.

Installation:

Once the project is downloaded to disk:

Download the files from https://www.cvlibs.net/datasets/kitti/raw_data.php

dataset 2011_09_26_drive_0013 marked as:

[synced + rectified_data], [calibration], and [tracklets]

and arranged in the project directory according to the following scheme:

2011_09_26 the main folder and inside:

     2011_09_26_drive_0013_extract_sync

         image_00

         image_01

         image_02

         image_03

         oxts

         velodyne_points

     calib_cam_to_cam.txt

     calib_imu_to_velo.txt

     calib_velo_to_cam.txt

Test:

python CarDistanceComparison_Lidar_Yolo26depth,py

Each frame appears on the screen, with the detected car in a box and the distance estimated by the lidar in black and the estimated distance in blue. by yolo26depth. You have to close each frame for the test to advance to the next.

A list will appear in the console indicating the differences found between the frames.


Python 3.12.13 | packaged by Anaconda, Inc. | (main, Jul  9 2026, 14:26:47) [MSC v.1942 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:\CarDistanceComparison_Lidar_Yolo26deph\CarDistanceComparison_Lidar_Yolo26depth.py

Distance acording Lidar: 6.53m Distance according vision: 5.94m TotalDife :0.59m Media :0.59m

Distance acording Lidar: 6.52m Distance according vision: 5.77m TotalDife :1.35m Media :0.67m

Distance acording Lidar: 6.24m Distance according vision: 5.10m TotalDife :2.48m Media :0.83m

Distance acording Lidar: 5.16m Distance according vision: 4.56m TotalDife :3.08m Media :0.77m

Distance acording Lidar: 4.99m Distance according vision: 5.33m TotalDife :3.42m Media :0.68m

Distance acording Lidar: 4.74m Distance according vision: 5.69m TotalDife :4.37m Media :0.73m

Distance acording Lidar: 5.11m Distance according vision: 6.58m TotalDife :5.85m Media :0.84m

Distance acording Lidar: 5.40m Distance according vision: 7.03m TotalDife :7.47m Media :0.93m

Distance acording Lidar: 5.75m Distance according vision: 7.76m TotalDife :9.48m Media :1.05m

Distance acording Lidar: 6.04m Distance according vision: 8.80m TotalDife :12.24m Media :1.22m

Distance acording Lidar: 6.41m Distance according vision: 9.09m TotalDife :14.92m Media :1.36m

Distance acording Lidar: 6.67m Distance according vision: 9.61m TotalDife :17.85m Media :1.49m

Distance acording Lidar: 7.24m Distance according vision: 8.62m TotalDife :19.24m Media :1.48m

Distance acording Lidar: 7.56m Distance according vision: 9.24m TotalDife :20.92m Media :1.49m

Distance acording Lidar: 7.88m Distance according vision: 10.23m TotalDife :23.27m Media :1.55m

Distance acording Lidar: 8.21m Distance according vision: 9.77m TotalDife :24.83m Media :1.55m

Distance acording Lidar: 8.54m Distance according vision: 10.22m TotalDife :26.51m Media :1.56m

Distance acording Lidar: 8.88m Distance according vision: 10.78m TotalDife :28.41m Media :1.58m

Distance acording Lidar: 9.21m Distance according vision: 10.77m TotalDife :29.96m Media :1.58m

Distance acording Lidar: 9.56m Distance according vision: 12.12m TotalDife :32.52m Media :1.63m

Distance acording Lidar: 9.91m Distance according vision: 12.71m TotalDife :35.32m Media :1.68m

Distance acording Lidar: 10.26m Distance according vision: 12.51m TotalDife :37.57m Media :1.71m

Distance acording Lidar: 10.64m Distance according vision: 12.23m TotalDife :39.16m Media :1.70m

Distance acording Lidar: 11.01m Distance according vision: 12.39m TotalDife :40.54m Media :1.69m

Distance acording Lidar: 11.37m Distance according vision: 11.81m TotalDife :40.99m Media :1.64m

Distance acording Lidar: 8.82m Distance according vision: 4.13m TotalDife :45.68m Media :1.76m

Distance acording Lidar: 11.75m Distance according vision: 12.99m TotalDife :46.92m Media :1.74m

Distance acording Lidar: 9.47m Distance according vision: 5.70m TotalDife :50.69m Media :1.81m

Distance acording Lidar: 12.14m Distance according vision: 14.47m TotalDife :53.02m Media :1.83m

Distance acording Lidar: 10.02m Distance according vision: 4.89m TotalDife :58.15m Media :1.94m

Distance acording Lidar: 12.53m Distance according vision: 14.27m TotalDife :59.89m Media :1.93m

Distance acording Lidar: 9.74m Distance according vision: 4.92m TotalDife :64.71m Media :2.02m

Distance acording Lidar: 12.90m Distance according vision: 13.04m TotalDife :64.85m Media :1.97m

Distance acording Lidar: 8.57m Distance according vision: 4.98m TotalDife :68.45m Media :2.01m

Distance acording Lidar: 7.78m Distance according vision: 5.01m TotalDife :71.22m Media :2.03m

Distance acording Lidar: 13.32m Distance according vision: 13.64m TotalDife :71.54m Media :1.99m

Distance acording Lidar: 7.27m Distance according vision: 4.94m TotalDife :73.86m Media :2.00m

Distance acording Lidar: 13.71m Distance according vision: 13.15m TotalDife :74.42m Media :1.96m

Distance acording Lidar: 6.69m Distance according vision: 6.06m TotalDife :75.05m Media :1.92m

Distance acording Lidar: 14.12m Distance according vision: 14.09m TotalDife :75.07m Media :1.88m

Distance acording Lidar: 4.79m Distance according vision: 6.22m TotalDife :76.51m Media :1.87m

Distance acording Lidar: 14.53m Distance according vision: 14.26m TotalDife :76.78m Media :1.83m

Distance acording Lidar: 4.65m Distance according vision: 6.53m TotalDife :78.67m Media :1.83m

Distance acording Lidar: 14.93m Distance according vision: 13.15m TotalDife :80.45m Media :1.83m

Distance acording Lidar: 4.66m Distance according vision: 6.27m TotalDife :82.06m Media :1.82m

Distance acording Lidar: 15.34m Distance according vision: 14.53m TotalDife :82.88m Media :1.80m

Distance acording Lidar: 4.90m Distance according vision: 6.31m TotalDife :84.29m Media :1.79m

Distance acording Lidar: 15.77m Distance according vision: 14.45m TotalDife :85.60m Media :1.78m

Distance acording Lidar: 5.20m Distance according vision: 7.24m TotalDife :87.64m Media :1.79m

Distance acording Lidar: 16.19m Distance according vision: 15.40m TotalDife :88.43m Media :1.77m

Distance acording Lidar: 5.60m Distance according vision: 7.68m TotalDife :90.51m Media :1.77m

Distance acording Lidar: 6.31m Distance according vision: 7.62m TotalDife :91.83m Media :1.77m

Distance acording Lidar: 17.39m Distance according vision: 16.08m TotalDife :93.14m Media :1.76m

Distance acording Lidar: 6.69m Distance according vision: 8.55m TotalDife :94.99m Media :1.76m

Distance acording Lidar: 17.80m Distance according vision: 16.31m TotalDife :96.48m Media :1.75m

Distance acording Lidar: 6.93m Distance according vision: 9.11m TotalDife :98.66m Media :1.76m

Distance acording Lidar: 18.21m Distance according vision: 18.18m TotalDife :98.69m Media :1.73m

Distance acording Lidar: 7.28m Distance according vision: 8.76m TotalDife :100.17m Media :1.73m

Distance acording Lidar: 7.48m Distance according vision: 9.71m TotalDife :102.40m Media :1.74m

Distance acording Lidar: 7.81m Distance according vision: 10.67m TotalDife :105.26m Media :1.75m

Distance acording Lidar: 8.14m Distance according vision: 10.77m TotalDife :107.89m Media :1.77m

Distance acording Lidar: 8.49m Distance according vision: 10.53m TotalDife :109.92m Media :1.77m

Distance acording Lidar: 8.83m Distance according vision: 10.72m TotalDife :111.82m Media :1.77m

Distance acording Lidar: 9.18m Distance according vision: 10.65m TotalDife :113.29m Media :1.77m

Distance acording Lidar: 9.52m Distance according vision: 11.32m TotalDife :115.10m Media :1.77m

Distance acording Lidar: 9.88m Distance according vision: 10.31m TotalDife :115.52m Media :1.75m

Distance acording Lidar: 10.22m Distance according vision: 12.80m TotalDife :118.10m Media :1.76m

Distance acording Lidar: 10.59m Distance according vision: 12.38m TotalDife :119.90m Media :1.76m

Distance acording Lidar: 10.96m Distance according vision: 12.75m TotalDife :121.68m Media :1.76m

Distance acording Lidar: 11.32m Distance according vision: 12.44m TotalDife :122.80m Media :1.75m

Distance acording Lidar: 11.70m Distance according vision: 12.63m TotalDife :123.74m Media :1.74m

Distance acording Lidar: 12.06m Distance according vision: 13.47m TotalDife :125.15m Media :1.74m

Distance acording Lidar: 12.44m Distance according vision: 11.81m TotalDife :125.77m Media :1.72m

Distance acording Lidar: 12.81m Distance according vision: 10.51m TotalDife :128.07m Media :1.73m

Distance acording Lidar: 13.17m Distance according vision: 11.93m TotalDife :129.31m Media :1.72m

Distance acording Lidar: 13.53m Distance according vision: 12.28m TotalDife :130.56m Media :1.72m

Distance acording Lidar: 13.89m Distance according vision: 12.66m TotalDife :131.80m Media :1.71m

Distance acording Lidar: 14.59m Distance according vision: 12.08m TotalDife :134.31m Media :1.72m


Conclusions:

- There is an estimated average difference of 1.72m between the distances estimated by lidar and those estimated by the YOLO26-Depth vision system.
- The series of frames included in the KITTI dataset are not of sufficient quality, which negatively impacts the YOLO26-Depth vision-based estimates.

# Improvements to incorporate:

Perform an adjustment using the YOLO26-Depth model.calibrate function, which requires selecting and training a set of approximately 100 images with their cars labeled and incorporating the distance to the YOLO coordinates x1, y1, x2, y2. This would initially require some fieldwork.

* This project received assistance from Google Gemini for the design of data processing scripts, hyperparameter optimization, and structuring of the calibration flow for YOLO26-Depth.

* Thanks to **Ultralytics** for providing the framework and native depth estimation tools.

Citation
@article{Geiger2013IJRR,
author = {Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel Urtasun},
title = {Vision meets Robotics: The KITTI Dataset},
journal = {International Journal of Robotics Research (IJRR)},
year = {2013}
}

@misc{googlegemini2026,
author = {Google},
title = {Gemini (Large Language Model)},
year = {2026},
howpublished = {\url{https://google.com}},
note = {Assistance in code optimization and dataset preparation for YOLO26-Depth}
}g Lidar: 12.90m Distance according vision: 13.04m TotalDife :64.85m Average :1.97m
