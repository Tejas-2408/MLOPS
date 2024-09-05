## Multi processing -> Process that run in parallel
'''
1. CPU-Bound task -> Tasks that are heavy on CPU usage(mathematical computations)
2. Parallel execution-> Multiple cores of the cpu
'''

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i*i*i}')


# Creating processes
p1 = multiprocessing.Process(target=square_numbers)
p2 = multiprocessing.Process(target=cube_numbers)

t = time.time()
p1.start()
p2.start()

## Wait for process completion and join back
p1.join()
p2.join()

finishedTime = time.time()-t
print(finishedTime)