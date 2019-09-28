import time
from concurrent.futures import ProcessPoolExecutor


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


start = time.time()
measure(lambda: ask_user())
measure(lambda: complex_calc())
print(f'Single thread total time: {time.time() - start}')

start = time.time()
with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calc)
    pool.submit(complex_calc)

print(f'Two thread total time: {time.time() - start}')
