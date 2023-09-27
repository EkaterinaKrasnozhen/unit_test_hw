
START = 25
finish = 100


def numver_interval(num):
    try:
        if 25 <= num <= 100:
            return True
        return False
    except TypeError:
        return 'Введено неверное значение'

