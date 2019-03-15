print("Hello World")
print("-----------------------")

name = "Cookie"
age = "30"
is_male = True
print("This is " + name)
print("He was " + age + " years old.")
print("He is male : " + str(is_male))
print("-----------------------")

doc = "This is doc."
print(doc)
print("-----------------------")

lower = "ABCDEFG"
print(lower + " change to upper : " + lower.lower())
print("-----------------------")

upper = "abcdeft"
print(upper + " change to lower : " + lower.upper())
print("-----------------------")

print(lower.isupper())
print("Is this upper ? " + str(lower.isupper()))
print("-----------------------")

is_upper_false = "aABCDEFG"
print(is_upper_false.isupper())
print("Is this upper ? " + str(is_upper_false.isupper()))
print("-----------------------")

len_src = "abcdefghijklmn"
print(len(len_src))
print(len_src[0])
print(len_src[13])
print(len_src[1:4])
print("-----------------------")

print(len_src.index("b"))
print(len_src.index("cde"))
print("-----------------------")

print(len_src.replace("a", "1"))
