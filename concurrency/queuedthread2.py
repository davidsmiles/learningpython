import queue

from threading import Thread

counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()


def increment_manager():
    global counter

    while True:
        increment = counter_queue.get()
        old_counter = counter
        counter = increment + old_counter
        job_queue.put((f'Running code {counter}', '------------------'))
        counter_queue.task_done()


Thread(target=increment_manager, daemon=True).start()


def print_manager():
    while True:
        message = job_queue.get()

        for line in message:
            print(line)

        job_queue.task_done()


Thread(target=print_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


worker_threads = [Thread(target=increment_counter) for thread in range(10)]
for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()
