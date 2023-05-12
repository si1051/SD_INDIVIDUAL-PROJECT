import sys


class Game:
    def __init__(self, q) -> None:
        self.q = q

    def startGame(self):
        current_question = list(self.q)[0]

        return current_question

    def restartGame(self):
        a = input("Try again? ").lower()
        if a != "yes":
            self.endGame()
        else:
            return self.startGame()

    def endGame(self):
        sys.exit()