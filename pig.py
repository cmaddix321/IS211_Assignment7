import random


class Pig:
    def __init__(self, playerScore=0, computerScore=0, turnScore=0):
        self.playerScore = playerScore
        self.computerScore = computerScore
        self.turnScore = turnScore

    def turn(self):

        play = input("Roll or Hold? ")
        if play == 'r':
            dice = random.randint(1, 6)
            print("The player rolled " + str(dice))
            if dice == 1:
                self.turnScore = 0
                self.computer_turn()
            else:
                self.turnScore += dice

        elif play == 'h':
            print('The player choose to hold')
            self.playerScore += self.turnScore
            self.turnScore = 0
            if self.playerScore >= 100:
                print(" Congratulation you won!!!")
                self.turnScore = 0
                self.computerScore = 0
                self.playerScore = 0
                self.play_game()

            self.computer_turn()

        elif play == "s":
            print("Player total :{0}".format(str(self.playerScore)))
            print("Computer total :{0}".format(str(self.computerScore)))
            print("Turn total :{0}".format(str(self.turnScore)))
            print("\n")

        else:
            print('Invalid input')

        pass

    def computer_turn(self):

        print("The computer plays")

        if self.turnScore == 0:
            choice = 1

        else:
            choice = random.randint(1, 2)

        if choice == 1:
            print("The computer chooses to roll")
            dice = random.randint(1, 6)
            print("The computer rolled " + str(dice))

            if dice == 1:
                self.turnScore = 0
                self.turn()

            else:
                self.turnScore += dice
                print("Computer's turn total is {0}".format(str(self.turnScore)))
                self.computer_turn()

        elif choice == 2:
            print("The computer choose to hold")
            self.computerScore += self.turnScore
            self.turnScore = 0
            print("Computer hold")
            if self.computerScore >= 100:
                print("The computer won!")
                self.turnScore = 0
                self.computerScore = 0
                self.playerScore = 0
                self.play_game()
            self.turn()

    pass

    def play_game(self):
        while (self.playerScore < 100) or (self.computerScore < 100):

            self.turn()


def main():

    game = Pig()

    game.play_game()


if __name__ == "__main__":
    main()
    pass
