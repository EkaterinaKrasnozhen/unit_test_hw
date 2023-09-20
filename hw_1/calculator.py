
class Calculator:
    
    def culculator() -> int:
        result = 0
        operator = input('Введите опаретора (+, -, *, /)')
        num1 = input('Введите певрое число')
        num2 = input('Введите второе число')
        match operator:
            case '+':
                result = int(num1) + int(num2)
            case '-':
                result = int(num1) - int(num2)
            case '*':
                result = int(num1) * int(num2)
            case '/':
                if (num2 != 0): 
                    result = float(num1) / float(num2)
                else:
                    raise ZeroDivisionError("Division by zero is not possible")   
            case _:
                raise RuntimeError("Unexpected value operator: " + operator)
        
        return result
    
    
if __name__ == '__main__':
    calc = Calculator
    print(calc.culculator())