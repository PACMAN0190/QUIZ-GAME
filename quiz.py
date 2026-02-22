from json import JSONDecoder

questions = (
    "how many elements are in the periodic table:",
    "which animal lays the largest eggs?:",
    "what is the most abundant gas in earth's atmosphere?:",
    "how many bones are in the human body?:",
    "which planet in the solar system is the hottest?:"
)

options = (
    ("A.116", "B.117", "C.118", "D.119"),
    ("A. Whale", "B. crocodile", "C. elephant", "D. tiger"),
    ("A. nitrogen", "B. oxygen", "C. carbon-dioxide", "D. hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. mercury", "B. venus", "C. earth", "D. mars")
)

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("correct ✅")
    else:
        print("incorrect ❌")
        print("Correct answer is:", answers[question_num])

    question_num += 1
print("------------------------")
print("      RESULTS           ")
print("------------------------")
print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")





print("                                    ")
print("------------------------")
print("Final score:", score, "/", len(questions))



