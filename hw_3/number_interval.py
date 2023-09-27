# Задание 2.

# Разработайте и протестируйте метод numberInInterval, 
# который проверяет, попадает ли переданное число в интервал (25;100).
START = 25
finish = 100

def numver_interval(num):
    try:
        if 25 <= num <= 100:
            return True
        return False
    except TypeError:
        return 'Введено неверное значение'
    
    
#print(numver_interval(0.234))