import random


class Main:
    def __init__(self):
        self.userNum1 = ""
        self.userNum2 = ""
        self.ComputerGuessedNumber = int
        self.Count = 0
        self.UserInputValidity = True
        self.CompAnsValidity = True
        self.UserAns = ""
        self.ComputerGuesses = {0}
        self.take_input()

    def take_input(self):
        self.UserInputValidity = True
        try:
            self.userNum1 = int(input("Enter a number to start with : "))
            self.userNum2 = int(input("Enter a number to End with : "))
        except ValueError:
            self.UserInputValidity = False
            print("Please enter numbers only")

        if not self.UserInputValidity:
            self.take_input()
        elif self.userNum1 > self.userNum2:
            print("Start number should be lesser than end number.")
            self.take_input()
        else:
            self.GenerateNumber(self.userNum1,self.userNum2)

    def GenerateNumber(self,num1,num2):
            self.ComputerGuessedNumber = random.randint(int(num1), int(num2))

            if self.ComputerGuessedNumber in self.ComputerGuesses:
                self.GenerateNumber(num1, num2)

            print("Computer Guessed Number = "+str(self.ComputerGuessedNumber))
            self.CheckCGNValidity()


    def CheckCGNValidity(self):
        self.ComputerGuesses.add(self.ComputerGuessedNumber)
        self.UserAns = input(f"\nThe number {self.ComputerGuessedNumber} guessed by computer is (Less = 1, Greater = 2, "
                             f"Equal = 3) than your guess: ")
        if (self.ComputerGuessedNumber == self.userNum1) and self.UserAns == "2":
            print("Invalid Answer")
            exit(1111)
        elif (self.ComputerGuessedNumber == self.userNum1) and self.UserAns == "1":
            print("Invalid Answer")
            exit(1111)
        elif (self.ComputerGuessedNumber == self.userNum2) and self.UserAns == "1":
            print("Invalid Answer")
            exit(1110)
        elif (self.ComputerGuessedNumber == self.userNum2) and self.UserAns == "2":
            print("Invalid Answer")
            exit(1110)
        elif self.UserAns == "1":
            self.userNum1 = self.ComputerGuessedNumber
            self.GenerateNumber(self.userNum1,self.userNum2)
        elif self.UserAns == "2":
            self.userNum2 = self.ComputerGuessedNumber
            self.GenerateNumber(self.userNum1,self.userNum2)
        elif self.UserAns == "3":
            print("The computer guessed the number right")
            exit()
        else:
            print("Enter a Valid Answer")
            self.CheckCGNValidity()


game = Main()
