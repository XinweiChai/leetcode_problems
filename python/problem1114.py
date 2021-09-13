import threading


class Foo:
    def __init__(self):
        self.first_barrier = threading.Barrier(2)
        self.second_barrier = threading.Barrier(2)

    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird):
        self.second_barrier.wait()
        printThird()


def printFirst():
    print('First', end="")


def printSecond():
    print('Second', end="")


def printThird():
    print('Third', end="")


if __name__ == '__main__':
    f = Foo()
    d = {1: (f.first, printFirst), 2: (f.second, printSecond), 3: (f.third, printThird)}
    for i in [2, 3, 1]:
        x = threading.Thread(target=d[i][0], args=(d[i][1],))
        x.start()
