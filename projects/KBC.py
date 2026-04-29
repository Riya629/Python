#program for KBC(Kaun banega corepati)

print("Your game starts now....")
print("\n")

print("\n")
Question=[
"Q1. Which keyword is used to define a function in Python?",
"Q2. What is the output of print(2 + 3)?",
"Q3. Which data type is immutable?",
"Q4. Which symbol is used for comments in Python?",
"Q5. What is the output of 10//3?"
]
Options=[
"A.func  B.define  C.def  D.function",
"A.23  B.5  C.6  D.Error",
"A. List B. Dictionary C. Tuple D. Set",
"A.//  B.#  C.--  D./* */  ",
"A.3.33  B.3  C.4  D.Erro "
 ]
Amount=0
Answer=["C", "B", "C", "B", "B"]
for i in range(len(Question)):
    print(Question[i])
    print(Options[i])

    user_answer=input("Enter your choice: ")
    if(user_answer.upper()==Answer[i]):
        print("Correct answer")
        Amount=Amount+1000
    else:
        print("Incorrect answer")

print("You won total",score,"Prize")


# printing prize after each correct answers
print("The questions are on your screen")
print("\n")
Questions = [
    "Q1. Which keyword is used to define a function in Python?",
    "Q2. What is the output of print(2 + 3)?",
    "Q3. Which data type is immutable?",
    "Q4. Which symbol is used for comments in Python?",
    "Q5. What is the output of 10//3?",
]

Options = [
    "A.func  B.define  C.def  D.function",
    "A.23  B.5  C.6  D.Error",
    "A. List B. Dictionary C. Tuple D. Set",
    "A.//  B.#  C.--  D./* */  ",
    "A.3.33  B.3  C.4  D.Erro ",
]

Answers = ["C", "B", "C", "B", "B"]
Amount = 0
for i in range(len(Questions)):
    print(Questions[i])
    print(Options[i])
    print("\n")
    user_answer = input("Enter your choice:")
    if user_answer.upper() == Answers[i]:
        Amount = Amount + 5000
        print("Correct answer You won", Amount)
        print("\n")
    else:
        print("Incorrect answers")
        print("\n")
    
print("You won total", Amount, "Amount")
