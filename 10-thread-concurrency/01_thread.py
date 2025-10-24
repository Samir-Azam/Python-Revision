import threading
import time

def take_order():
    for item in range(1, 4):
        print(f"Taking order for #{item}")
        time.sleep(1)

def prepare_order():
    for item in range(1, 4):
        print(f"Perparing order for #{item}")
        time.sleep(2)

thread1 = threading.Thread(target = take_order)
thread2 = threading.Thread(target = prepare_order)

thread1.start()
thread2.start()

# join makes the main thread to wait untill both the threads are executed
thread1.join()
thread2.join()