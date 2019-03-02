is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    ## Both False
    print("You neither male non tall")

if is_male and is_tall:
    ## Both True
    print("You are a male or tall or both")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You neither male non tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(10, 5, 70))


def src_equal(src1, src2):
    if src1 == src2:
        print("equal")
    else:
        print("not equal")


src_equal("aaa", "aaa")

num1 = float(input("Enter num1:"))
op = input("Enter operator:")
num2 = float(input("Enter num2:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
