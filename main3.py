from ultralytics import YOLO
import cv2
import math
import threading
import serial
import time
import numpy as np
import atexit

model = YOLO("yolo-Weights/yolov8m.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


signal_queue = []

count = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
}
   



def detect_vechile(cam_num, cap):  # Camera 1
    ret1, img1 = cap.read()
    results = model.predict(img1, stream=True, classes=[2])
    for r in results:
            boxes = r.boxes
            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img1, (x1, y1), (x2, y2), (255, 0, 255), 3)

                if cam_num == 1:
                    count.update({
                    "a": len(boxes)
                })
                else:
                    count.update({
                    "c": len(boxes)
                })

    # Display the frames from both cameras
    cv2.imshow('Webcam', img1)
    cv2.waitKey(0)
    # if cv2.waitKey(1) == ord('q'):
    #     break






def detect_wrapper():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    detect_vechile(cam_num=1, cap=cap1)
    detect_vechile(cam_num=2, cap=cap2)

    print(count)
    threading.Timer(10, detect_wrapper).start()

detect_wrapper()