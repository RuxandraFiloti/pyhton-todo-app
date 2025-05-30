import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, '-', alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice
   

score = 0

for question in data:
        if question["user_choice"] == question["correct_answer"]:
            score = score + 1
            result = "Correct Answer"
        else: 
             result = "Wrong Answer"
        message = f"{result} Your answer is: {question['user_choice']}, Correct answer is: {question['correct_answer']}"
        print(message)