questions = ['1. How many ghosts at the start of the Pac-Man?',
             '2. What sports car company manufactures the 911?',
             '3. What is the newest meme state in USA?',
             '4. What is the most hated game?',
             '5. What is the latest gaming console that SEGA released?']
answers = ["4", "Porsche", "Ohio", "Popular", "Dreamcast"]
user_choice = str("")
qindex = int(len(questions) - 5)
a = int(0)


def game(question, qindex):
    print("--------------")
    # question_index: int = random.randint(0, len(questions) - 1)
    print(question[qindex])
    user_choice = input(str("Answer: "))
    return user_choice


print("------Quiz!------")
for i in range(0, 5, 1):
    if game(questions, qindex) == str(answers[qindex]):
        print("True")
        a += 1
    else:
        print("False")
    qindex += 1
    i += 1
print("-----------------")
print(f"Correct answers - {a}")
print(f'Answers: {answers}')
