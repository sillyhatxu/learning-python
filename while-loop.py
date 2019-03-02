i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess:")
    print(guess)

print("You Win!!!")