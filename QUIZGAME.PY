questions=("WHAT IS THE CAPITAL OF INDIA:",
           "WHAT IS THE COLOUR OF THE SKY?",
           "WHAT IS THE LARGEST MAMMAL ON EARTH?")
options=(("A) NEW DELHI","B) MUMBAI","C) KOLKATA"),
         ("A) GREEN","B) BLUE","C) RED"),
         ("A) ELEPHANT","B) WHALE","C) GIRAFFE"))
answers=("A","B","B")
guesses=[]
score=0
question_num=0
for question in questions:
    print("--------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter your guess(A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer.")
            
    question_num+=1
print("--------------")
print("----result----")
print("--------------")
print(f"answers are\n{answers}")
print(f"guesses are\n{guesses}")

score=(score/len(questions))*100
print(f"your score is {score}%")