friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
print(friends[2])

print(friends[2:4])
friends[1] = "Lily"
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
bad_src = ["heihei", "haha", "hehe"]

friends.extend(lucky_numbers)
print(friends)

friends.append(bad_src)
print(friends)

friends.insert(1, "Kelly")
print(friends)
friends.remove("Kelly")
print(friends)
friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()  # remove last string
print(friends)

print(friends.index("Jim"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)
lucky_numbers = [23, 42, 4, 8, 15, 16]
lucky_numbers.sort()
print(lucky_numbers)

friends2 = friends.copy()
print(friends)
print(friends2)

coordinates = (4, 5)
print(coordinates[0])
## we can't change value
# coordinates[1] = 5

coordinates = [(4, 5),(6,7),(80,34)]
print(coordinates)
print(coordinates[0])
