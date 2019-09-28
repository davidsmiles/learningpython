import time
from concurrent.futures import ThreadPoolExecutor


def measure(func):
    start = time.time()
    func()
    end = time.time()
    print(f'{func.__name__} -took {end - start}')


def ask_user():
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)


def complex_calc():
    print('Started calculating...')
    [x**2 for x in range(20000000)]


if __name__ == '__main__':
    start = time.time()
    measure(lambda: ask_user())
    measure(lambda: complex_calc())
    print(f'Single thread total time: {time.time() - start}')

    start = time.time()

    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calc)
        pool.submit(ask_user)

    print(f'Two thread total time: {time.time() - start}')

    # thread1 = Thread(target=complex_calc)
    # thread2 = Thread(target=ask_user)
    #
    # start = time.time()
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()
    #
    # print(f'Two thread total time: {time.time() - start}')
