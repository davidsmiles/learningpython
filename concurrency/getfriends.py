friends = ['David', 'James', 'Ugbero', 'Fadilah', 'Emmanuel']


def get_friends():
    yield from friends


pal = get_friends()
print(next(pal))
print(next(pal))