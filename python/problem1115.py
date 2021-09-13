import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_foo = threading.Lock()
        self.lock_bar = threading.Lock()
        self.lock_bar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lock_foo.acquire()
            printFoo()
            self.lock_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lock_bar.acquire()
            printBar()
            self.lock_foo.release()


def printFoo():
    print('foo', end="")


def printBar():
    print('bar', end="")


if __name__ == '__main__':
    x = FooBar(2)
    t1 = threading.Thread(target=x.foo, args=(printFoo,))
    t2 = threading.Thread(target=x.bar, args=(printBar,))
    t1.start()
    t2.start()
