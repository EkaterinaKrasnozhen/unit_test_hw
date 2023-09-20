TOTAL = 100

class Calculator:
    
    def culculator(operator: str, num1: int, num2: int) -> float:
        result = 0
        match operator:
            case '+':
                result = float(num1) + float(num2)
            case '-':
                result = float(num1) - float(num2)
            case '*':
                result = float(num1) * float(num2)
            case '/':
                # if (num2 != 0): 
                #     result = float(num1) / float(num2)
                # else:
                #     raise ZeroDivisionError("Division by zero is not possible")   # и так выдает ZeroDivision без raise
                result = float(num1) / float(num2)
            case _:
                raise RuntimeError(f"Неверно введен оператор")
                
        return result
        
    
    def calculate_discount(sum: float, discount: float) -> float:
        if discount < 0:
            raise RuntimeError(f"Скидка должна быть больше 0")
        res = sum - ((sum / TOTAL) * discount)
        return res
    
    
if __name__ == '__main__':
    calc = Calculator
    print(calc.culculator('*', 4, 2))
    print(calc.calculate_discount(100, -1))