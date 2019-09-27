def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10), countdown(5), countdown(20)]
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')


class Countdown:
    def __init__(self, c):
        self.count = c

    def __next__(self):
        if self.count > 0:
            i = self.count
            i -= 1
            self.count = i
            return self.count
        else:
            raise StopIteration

    def __iter__(self):
        return self


c = Countdown(25)
