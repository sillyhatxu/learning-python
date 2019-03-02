try:
    number = int(input("Enter number: "))
    print(number)
except:
    print("Invalid Input")

try:
    value = 10 / 0
    number = int(input("Enter number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero;", err)
except ValueError:
    print("Invalid Input")
