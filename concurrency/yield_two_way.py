from collections import deque

friends = deque(('Rolf', 'David', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass


friends_gen = get_friend()
g = greet(friends_gen)

print(next(g))
print(next(g))
