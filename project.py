from enum import Flag
import re


class hangman:

    def __init__(self):

        self.list1 = ["Vehical", "Body Part", "Laptop", "Flower", "Pakistan"]
        self.list2 = ["truck", "brain", "lenovo", "orchid", "islamabad"]
        self.allowError = None
        self.guesses = []
        self.guess = None
        self.size = 5
        self.flag1 = None
        self.flag = None


    def displayFunc(self, word):

        for letter in word:
            if(letter.lower() in self.guesses): 
                print(letter , end = " ")
            else:
                print("_", end = " ")


    def inputChar(self):

        done = False
        while not done:

            self.guess = input(f"{self.allowError} allow errors are left, Enter charactor: ")

            if not len(self.guess) == 1:
                print("Only one charactor allowed! Try Again")
                done = False
            elif not re.match("^[a-z]*$", self.guess):
                print("Error! Only letters a-z allowed! Try Again")
                done = False
            else:
                done = True    

        self.guesses.append(self.guess.lower())  



    def errorCalculation(self, word):

        if (self.guess.lower() not in word.lower()):
            self.allowError -= 1
                    
            if(self.allowError == 0):
                loop = False
                return loop


    def result(self, word):

        if self.flag :
            print(f"You Win. The word is {word}")
            print("")
        else:
            print(f"You Lose. The word is {word}")
            print("")

    def playAgain(self):

        key = input("Do you want to play agian? if yes the press 'y': ")
            
        if(key == 'y'):
            self.flag1 = True
            return self.flag1
        else:
            self.flag1 = False
            return self.flag1

            

    def hangmanFunc(self):
        
        self.flag1 = True
        i = 0
        while (i < self.size and self.flag1 == True):

            print(self.list1[i])
            word = self.list2[i]  

            self.flag = False 
            self.allowError = 7        

            while not self.flag:

                self.displayFunc(word)
                print("")

                self.inputChar()
                
                if(self.errorCalculation(word) == False):
                    break

                self.flag = True

                for letter in word:
                    if letter.lower() not in self.guesses:
                        self.flag = False
                        
            self.result(word)
            self.guesses = []

            self.playAgain()

            i += 1


if __name__ == "__main__":

    obj = hangman()
    obj.hangmanFunc()
        



