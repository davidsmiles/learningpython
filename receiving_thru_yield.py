from collections import deque
from types import coroutine

friends = deque(('Rolf', 'David', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        try:
            friend = friends.popleft().upper()
            greeting = yield
            print(f'{greeting} {friend}')
        except StopIteration:
            print('Finished')


async def greet(g):
    print('Starting...')
    await g
    print('Ending')
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')
greeter.send('How are you,')