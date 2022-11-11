from math import Calculator


calc = Calculator()

while True:
    print("Please enter the number of your operation: 1.Add  2.Subtraction   3.Multiplication    4.Division    5.Exit")
    op = int(input())
    print("Enter your first number:")
    a = float(input())
    print("Enter your second number:")
    b = float(input())

    if op==1:
        res = calc.add(a, b)
        print(f'The result is {res}')
    elif op==2:
        res = calc.subtract(a, b)
        print(f'The result is {res}')
    elif op==3:
        res = calc.multiply(a, b)
        print(f'The result is {res}')
    elif op==4:
        res = calc.divide(a, b)
        print(f'The result is {res}')
    elif op==5:
        break
    else:
        print("Please enter a valid number!")
