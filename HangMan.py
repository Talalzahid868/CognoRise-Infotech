import random
stages = [  """
                -----
                |   |
                    |
                    |
                    |
                   |
              --------
              """,
               """
                -----
                |   |
                O   |
                    |
                    |
                   |
              --------
              """,
              """
                -----
                |   |
                O   |
                |   |
                    |
                   |
              --------
              """,
                """
                -----
                |   |
                O   |
               /|   |
                    |
                   |
              --------
              """,
              """
                -----
                |   |
                O   |
               /|\\  |
                    |
                   |
              --------
              """,
                 """
                -----
                |   |
                O   |
               /|\\  |
               /    |
                   |
              --------
              """,
              """
                -----
                |   |
                O   |
               /|\\  |
               / \\  |
                   |
              --------
              """,
           ]


# print(stages[1])
# print(len(stages))
words=['python','hangman','programming','coding','developer']
word=random.choice(words).upper()
# print(word)
word_display=["_"]*len(word)
# print(word_display)
tries=6
guessed=[]

while tries>0:
    print(stages[6-tries])
    print("Display word : ",word_display)
    print("Tries left : ",tries)
    print("Guessed word:",guessed)
    w=input("Enter the letter").upper()
    if w in guessed:
        print("You have alraedy passed this word.")
        continue
    guessed.append(w)

    if w in word:
        print("Good Guess")
        for i in range(len(word)):
            if word[i]==w:
                word_display[i]=w
    else:
        print("Wrong Guess")
        tries-=1

    if "_" not in word_display:
        print("Congratulation You guess the word",word)
        break

else:
    print(stages[6])
    print("You have no more tries, you lost")    


  


    




