from calculator import Calculator


calc = Calculator

def test_calculate_discount_positive():
        assert calc.calculate_discount(100, 10) == 90, 'Тест с положительными числами провален'


def test_calculate_discount_zero():
        assert calc.calculate_discount(100, 0) == 100, 'Тест с нулевыми значениями провален'
        
        
def test_calculate_discount_negative():
    try:
        calc.calculate_discount(100, -10)
    except RuntimeError:
        print('Все тесты прошли')
        
        
    
if __name__ == '__main__':
    test_calculate_discount_positive()
    test_calculate_discount_negative()
    test_calculate_discount_zero()