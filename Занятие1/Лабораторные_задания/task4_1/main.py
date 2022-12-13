from itertools import count


def task():
    counter = count(100, 10)
    n = 0
    while n < 10:
        n +=1
        print(next(counter))


    # TODO распечатать с столбик первые 10 чисел бесконечного итератора


if __name__ == "__main__":
    task()
