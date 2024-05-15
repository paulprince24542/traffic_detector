# import serial.tools.list_ports

# ports = serial.tools.list_ports.comports()
# serialInst = serial.Serial()

# portsList = []

# for onePort in ports:
#     portsList.append(str(onePort))
#     print(str(onePort))
    
# val = input("Select Port: COM")

# for x in range(0, len(portsList)):
#     if portsList[x].startswith("COM" + str(val)):
#         portVar = "COM" + str(val)
#         print(portVar)

# serialInst.baudrate = 9600
# serialInst.port = portVar
# serialInst.open()

# if True:
#     print("Executing")
#     command = "signal1"
#     serialInst.write(command.encode('utf-8'))

# while True:
#     command = input("Arduino Command: (ON/OFF): ")
#     serialInst.write(command.encode('utf-8'))

#     if command == 'exit':
#         exit()
import threading
signal_queue = []
def detect_wrapper():
    print("Queue Length:", len(signal_queue))
    if(len(signal_queue) > 0):
            if(signal_queue[0] == 1):
                print("Enter Queue 1")
                signal_queue.pop(0)
            elif(signal_queue[0] == 2):
                print("Enter Queue 2")
                signal_queue.pop(0)
    else:

        car_count_1 = input("FIrst:")
        car_count_2 = input("Second:")
        if(car_count_1 > car_count_2):
            signal_queue.insert(1, 1)
            print(signal_queue)
        else:
            signal_queue.insert(2, 2)
            print(signal_queue)
        
    threading.Timer(10, detect_wrapper).start()

detect_wrapper()