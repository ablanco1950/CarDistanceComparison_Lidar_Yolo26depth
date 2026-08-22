# CarDistanceComparison_Lidar_Yolo26deph
Performs a comparison between distance data returned by a lidar and stored in KITTI (https://www.cvlibs.net/datasets/kitti/raw_data.php), dataset 2011_09_26_drive_0013, with car distance estimates from yolo26depth over the frames accompanying the lidar estimates.

Requirements:

pip install ultralytics pykitti opencv-python numpy

It is important to have the latest version of ultralytics; otherwise, the recently created yolo26 module may not be found.

Installation:

Once the project is downloaded to disk, locate the files named:

Download the corresponding files from https://www.cvlibs.net/datasets/kitti/raw_data.php

dataset 2011_09_26_drive_0013 marked as:

[synced + rectified_data], [calibration], and [tracklets]

and arranged according to the following scheme:

2011_09_26

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

Conclusions:

- There is an estimated average difference of 1.72m between the distances estimated by lidar and those estimated by the YOLO26-Depth vision system.
- The series of frames included in the KITTI dataset are not of sufficient quality, which negatively impacts the YOLO26-Depth vision-based estimates.

#Improvements to incorporate:

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
