def even_odd(num):
    try:
        return (num % 2 == 0)
    except TypeError:
        return 'Введено неверное значение'
