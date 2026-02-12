from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.semZero = Semaphore(1)
        self.semEven = Semaphore(0)
        self.semOdd = Semaphore(0)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            # Request permission to write a zero
            self.semZero.acquire()
            printNumber(0)

            # Check if i is even or odd, then give permission to write the number
            if i & 1:
                self.semOdd.release()
            else:
                self.semEven.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            # Request permission to write an even number
            self.semEven.acquire()
            printNumber(i)

            # Give permission to write zero
            self.semZero.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            # Request permission to write an odd number
            self.semOdd.acquire()
            printNumber(i)

            # Give permission to write zero
            self.semZero.release()
