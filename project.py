import re


class hangman:
    def __init__(self):
        self.list1 = ["Vehical", "Body Part", "Laptop", "Flower", "Pakistan"]
        self.list2 = ["truck", "brain", "lenovo", "orchid", "islamabad"]

    def hangmanFunc(self):
        
        size = 5
        flag1 = True
        i = 0
        while (i < size and flag1 == True):
            print(self.list1[i])
            word = self.list2[i]

            allowError = 7
            guesses = []
            
            flag = False

            while not flag:

                for letter in word:
                    if(letter.lower() in guesses): 
                        print(letter , end = " ")
                    else:
                        print("_", end = " ")

                print("")

                done = False
                while not done:
                    guess = input(f"{allowError} allow errors are left, Enter charactor: ")

                    if not len(guess) == 1:
                        print("Only one charactor allowed! Try Again")
                        done = False
                    elif not re.match("^[a-z]*$", guess):
                        print("Error! Only letters a-z allowed! Try Again")
                        done = False
                    else:
                        done = True    

                guesses.append(guess.lower())
                
                if (guess.lower() not in word.lower()):
                    allowError -= 1
                    
                    if(allowError == 0):
                        break

                flag = True

                for letter in word:
                    if letter.lower() not in guesses:
                        flag = False
                        

            if flag :
                print(f"You Win. The word is {word}")
                print("")
            else:
                print(f"You Lose. The word is {word}")
                print("")
            
            key = input("Do you want to play agian? if yes the press 'y': ")
            
            if(key == 'y'):
                flag1 = True
            else:
                flag1 = False

            i += 1


obj = hangman()
obj.hangmanFunc()


