for letter in "Griaffe Academy":
    print(letter)
print("----------")
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(len(friends))
print("----------")
for name in friends:
    print(name)
print("----------")
for index, name in enumerate(friends):
    print(index, name)
print("----------")
for index in range(10):
    print(index)
print("----------")
for index in range(3, 8):
    print(index)
print("----------")

for index in range(len(friends)):
    print(friends[index])
print("----------")

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")
print("----------")

letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in letter:
    if char.lower() in "asdfjklp":
        print(char)
