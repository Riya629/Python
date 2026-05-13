Questions = [
    [
        "Q1. Which keyword is used to define a function in Python?",
        "A.func  B.define  C.def  D.function",
    ],
    ["Q2. What is the output of print(2 + 3)?", "A.23  B.5  C.6  D.Error"],
    ["Q3. Which data type is immutable?", "A. List B. Dictionary C. Tuple D. Set"],
    ["Q4. Which symbol is used for comments in Python?", "A.//  B.#  C.--  D./* */  "],
    ["Q5. What is the output of 10//3?", "A.3.33  B.3  C.4  D.Erro "],
]

Answers = ["C", "B", "C", "B", "B"]
levels = [1000, 5000, 10000, 250000, 500000]
money = 0
for i in range(len(Questions)):
    print(Questions[i])
    print(f"Question for {levels[i]}")
    reply = input("Enter your choice A. B. C. D:")
    if reply.upper() == Answers[i]:
        money = money + levels[i]
        print(f"correct answer you won {money}")
    else:
        print("incorrect answers")
        break
