from random import randint


def hello():
    return 2 + 2


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def play_random():
    num = randint(0, 10)
    if num > 5:
        return "größer"
    return "kleiner"


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass


def print_me():
    print("hallo")


def is_not_flat(data):
    return any(isinstance(i, list) for i in data)


def sum_list(data):
    return sum(data)
