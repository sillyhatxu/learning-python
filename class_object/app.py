from class_object.Student import Student
import json

person = {
    'first_name': "John",
    "isAlive": True,
    "age": 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    },
    "hasMortgage": None
}

data = json.dumps(person)   # serialize

print(data)

student1 = Student("Jim", "Business", 3.8, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.to_json())

print(student1.gpa)
print(student2.gpa)

print(student1.on_honor_roll())
print(student2.on_honor_roll())

from class_object.Question import Question

question_prompts = [
    "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange\n\n",
    "What color are Bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow\n\n",
    "What color are strawberries? \n(a) Yellow\n(b) Red \n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)