import random
l=['rock','scissor','paper']

# user=str(input("Enter your choice (rock,scissor,paper):" )).lower()
# computer_choice=random.choice(l)
# print(user)
# print(computer_choice)
# if (user=='rock' and computer_choice=='scissor') or (user=='paper' and computer_choice=='rock') or (user=='scissor' and computer_choice=='scissor'):
#     print("You win!")
# elif user==computer_choice:
#     print("Draw")
# else:
#     print("You lose!")      

def userchoice():
    user=str(input("Enter your choice (rock,scissor,paper,quit):" )).lower()
    if user not in ['rock','scissor','paper','quit']:
        print("Please select the option which is given above")
    else:
        return user    
        

def ComputerChoice():
    comp=random.choice(l)
    return comp

def Determine_winner():
    user=userchoice()
    comp=ComputerChoice()
    if user=='quit':
        return "quit"
    if (user=='rock' and comp=='scissor') or (user=='paper' and comp=='rock') or (user=='scissor' and comp=='paper'):
        return "Youwin!"
    elif user==comp:
        return "Draw"
    else:
        return "You lose!" 
    
def scoring():
    w=''' Welcome to Rock, Scissors, Paper
          Instructions:
          --> Type 'Rock' or 'Scissors'or 'Paper' to make your choice
          --> Type 'quit' for exit the game 
'''
   
    print(w)
    user_score=0
    comp_score=0
    rounds=0
   
    while True:
        # u=userchoice()
        d=Determine_winner()
        if d=='quit':
            print("Thank you for playing game")
            print(f"User score: {user_score}" )
            print(f"Computer score: {comp_score}" )
            print(f"Game RoundS:{rounds}" )
            break

        if d=="Youwin!":
            user_score+=1
        elif d=="You lose!":
            comp_score+=1  

        rounds+=1
        print(f"User score: {user_score}" )
        print(f"Computer score: {comp_score}" )
        print(f"Game RoundS:{rounds}" )
        
scoring()            

     

            






    

