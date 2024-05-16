signal_queue = []


import threading


def set_queue():
    print(signal_queue)
    if len(signal_queue) > 0:
        if signal_queue[0] == 1:
            print("Queue 2")
        elif signal_queue[0] == 2:
            print("Queue 1")
    else:
        car_count_1 = 3
        car_count_2 = 4
        if car_count_1 > car_count_2:
            signal_queue.insert(1, 1)
            print("Queue 1")
        else:
            signal_queue.insert(2, 2)
            print("Queue 2")
    threading.Timer(15, set_queue).start()


set_queue()
