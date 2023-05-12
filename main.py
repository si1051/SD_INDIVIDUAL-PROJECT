from question import *
from game import Game
from answer import Answer

game = Game(q)
answer = Answer(q)

question = Question(game, answer)

while True:
    question.showQuestion()



