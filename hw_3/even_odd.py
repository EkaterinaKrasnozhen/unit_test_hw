# *Задание 1.

# Напишите тесты, покрывающие на 100% метод evenOddNumber, 
# который проверяет, является ли переданное число четным или нечетным

def even_odd(num):
    try:
        return  (num % 2 == 0)
    except TypeError:
        return 'Введено неверное значение'


#even_odd('f')
