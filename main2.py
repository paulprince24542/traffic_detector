from ultralytics import YOLO
import cv2
import math
import threading
import serial
import time
import numpy as np
import atexit



arduino = serial.Serial('COM7', 115200)
time.sleep(3)

signal_queue = []

# ! Load yolo modal
model = YOLO("yolo-Weights/yolov8m.pt")

def serialCommand(command):
    arduino.write(command.encode())
    # time.sleep(3)
    

def detect_vechiles(img, camera_num):
    print("Detecting")
    results = model.predict(img, classes=[2])
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        if camera_num == 1:
            count.update({
            "a": len(boxes)
        })
        else:
            count.update({
            "c": len(boxes)
        })
    cv2.imshow('Image', img)
    cv2.waitKey(0)  
    print(len(boxes))
    return img, len(boxes)
    

def detect_wrapper():
    
    # serialCommand("a")
    # serialCommand("d")

    serialCommand("d")
    in_1 = input("Enter first Image")
    in_2 = input("Enter second Image")
    cap_1 = cv2.imread(in_1)
    cap_2 = cv2.imread(in_2)
    # cap_1 = cv2.imread("image_1.jpg")
    # cap_2 = cv2.imread("image_2.jpg")

    # cv2.imshow('Image', cap_1)
    # cv2.waitKey(0) 
    # cv2.imshow('Image', cap_2)
    # cv2.waitKey(0)
   
    

   

    print("Signal Queue", signal_queue)
    if(len(signal_queue) > 0):
        if(signal_queue[0] == 1):
            print("Enter Queue 1")
            signal_queue.pop(0)
            serialCommand("c")
        elif(signal_queue[0] == 2):
            print("Enter Queue 2")
            signal_queue.pop(0)
            serialCommand("b")
    else:
        road_1, car_count_1 = detect_vechiles(cap_1, 1)
        road_2, car_count_2 = detect_vechiles(cap_2, 2)
        print("car_count_1:", car_count_1)
        print("car_count_2:", car_count_2)
        if(car_count_1 > car_count_2):

            signal_queue.insert(1, 1)
            serialCommand("b")
        else:
            signal_queue.insert(2, 2)
            serialCommand("c")
    
    
    threading.Timer(10, detect_wrapper).start()

def exit_handler():
    serialCommand("a")

       
count = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
}
   









detect_wrapper()

atexit.register(exit_handler)
