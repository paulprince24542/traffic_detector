import cv2
from ultralytics import YOLO
import math
import threading

import time
import numpy as np
import atexit
import os
import serial

arduino = serial.Serial("COM5", 115200)
time.sleep(3)


def serialCommand(command):
    arduino.write(command.encode())
    # time.sleep(3)


signal_queue = []

cap1 = cv2.VideoCapture(0)  # Camera 1
cap2 = cv2.VideoCapture(1)  # Camera 2


model = YOLO("yolo-Weights/yolov8l.pt")
classNames = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]
ret1, image_1 = cap1.read()
ret2, image_2 = cap2.read()

count = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
}


def detect(cam_num, image):
    results = model.predict(image, classes=[1, 2, 3, 4, 5, 7])
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 3)
        if cam_num == 1:
            count.update({"a": len(boxes)})
        else:
            count.update({"c": len(boxes)})
        print(count)
        return len(boxes)

    # cv2.imshow('Detected', image)


def main_capture():
    cap1 = cv2.VideoCapture(0)  # Camera 1
    cap2 = cv2.VideoCapture(1)  # Camera 2

    cap1.set(3, 640)
    cap1.set(4, 480)
    cap2.set(3, 640)
    cap2.set(4, 480)

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        cv2.imshow("Camera 1", frame1)
        cv2.imwrite("./capture/image1.jpg", frame1)
        cv2.imshow("Camera 2", frame2)
        cv2.imwrite("./capture/image2.jpg", frame2)
        if cv2.waitKey(1) == ord("q"):
            break

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


def wrap():
    serialCommand("a")

    print("Signal Queue", signal_queue)
    if len(signal_queue) > 0:
        if signal_queue[0] == 1:
            print("Queue 2")
            signal_queue.pop(0)
            serialCommand("b")
        elif signal_queue[0] == 2:
            print("Queue 1")
            signal_queue.pop(0)
            serialCommand("c")
    else:
        main_capture()
        image_1 = cv2.imread("./capture/image1.jpg")
        image_2 = cv2.imread("./capture/image2.jpg")
        car_count_1 = detect(1, image_1)
        car_count_2 = detect(2, image_2)
        print("car_count_1:", car_count_1)
        print("car_count_2:", car_count_2)
        if car_count_1 > car_count_2:
            print("Queue 1")
            signal_queue.insert(1, 1)
            serialCommand("c")
        else:
            print("Queue 2")
            signal_queue.insert(2, 2)
            serialCommand("b")

    threading.Timer(15, wrap).start()


wrap()
