def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}')

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Weel", "age": 30},
    {"name": "David James", "age": 21}
]

print(search(friends, "Adam Weel", lambda x: x["name"]))