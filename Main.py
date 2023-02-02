import sys
from Calc import Calculator

def main():
    calc = Calculator()
    while True:
        left_operand = input("Enter first operand or quit for exit\n")
        if(left_operand == 'quit'):
            print("Exiting from app")
            sys.exit()
            
        operator = input("Enter operator\n")
        right_operand = input("Enter second operand\n")
        try:
            print(calc.calculate([left_operand, operator, right_operand]))
        except ValueError:
            print("Wrong operator or bad operands")
        except ZeroDivisionError:
            print("Can't divide by zero")


if __name__ == '__main__':
    main()