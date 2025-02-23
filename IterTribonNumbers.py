import math

class TribonNumbersIterableWithGenerator:
    def __init__(self, size):
        self.x = size

    # метод получения итератора
    def __iter__(self):
        f1, f2, f3 = 1, 1, 1 #начальные значения

        for _ in range(self.x):
            yield f1
            f1, f2, f3 = f2, f3, f1 + f2 + f3

import time


if __name__ == '__main__':
    main_iter = TribonNumbersIterableWithGenerator(10)
    for line in main_iter:
        print(line)
        time.sleep(0.25)