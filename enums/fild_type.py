from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sun)
print(Weekday.Fri)

day = Weekday.Mon

print(day == Weekday.Mon)
print(day == Weekday.Wed)