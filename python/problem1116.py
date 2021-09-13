from threading import Barrier, Lock
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.barriers = [Barrier(2), Barrier(2)]
        self.zero_lock = Lock()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            self.ct += 1
            self.barriers[self.ct % 2].wait()

    def even(self, printNumber):
        for _ in range(self.n // 2):
            self.barriers[0].wait()
            printNumber(self.ct)
            self.zero_lock.release()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            self.barriers[1].wait()
            printNumber(self.ct)
            self.zero_lock.release()


def printNumber(x):
    print(x, end='')


if __name__ == '__main__':
    f = ZeroEvenOdd(3)
    t1 = threading.Thread(target=f.zero, args=(printNumber,))
    t2 = threading.Thread(target=f.odd, args=(printNumber,))
    t3 = threading.Thread(target=f.even, args=(printNumber,))
    t1.start()
    t2.start()
    t3.start()
