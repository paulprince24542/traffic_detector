from ultralytics import YOLO
import cv2
import math
import threading

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
   

def capture_image(cam_num,cap):
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow("image",frame)
            if(cam_num==1):
                cv2.imwrite('image1.jpg', frame)
            else:
                cv2.imwrite('image2.jpg', frame)
    cap.release()
    cv2.waitKey(0)

def detect_vechile(cam_num, img):  # Camera 1
    
    results = model.predict(img, stream=True, classes=[1,2,3,5,7])
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            if cam_num == 1:
                count.update({
                "a": len(boxes)
            })
            else:
                count.update({
                "c": len(boxes)
            })
                break
        print(count)
        cv2.imshow('Webcam', img)
        cv2.waitKey(0)



    
def detect_wrapper():
    cap1 = cv2.VideoCapture(0)
    capture_image(1, cap1)
    cap2 = cv2.VideoCapture(1)
    capture_image(2, cap2)

    
    img1 = cv2.imread("image1.jpg")
    detect_vechile(1,img1)
    img2 = cv2.imread("image2.jpg")
    detect_vechile(2,img2)
    # threading.Timer(10, detect_wrapper).start()

detect_wrapper()
