import random
import time
from threading import Thread

counter = 0


def increment_counter():
    global counter
    print(f'counter {counter} started...')
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print('-----------------------')
    print(f'counter {counter} finished...')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
