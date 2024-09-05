## Multi Threading
'''
1. I/o based task - task that spend more time waiting for I/o operations
2. Concurrent execution: when you want to improve the throughput of your application by performing multiple operations concocurently
'''

import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(i)

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

## Create Thread
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)

t = time.time()
t1.start()
t2.start()

## Join to main thread
t1.join()
t2.join()

fiinished_time = time.time()-t
print(fiinished_time)