
class Answer:
    def __init__(self, q) -> None:
        self.q = q

    def answerYes(self, current_question):
        current_question = self.q[current_question][0]

        return current_question

    def answerNo(self, current_question):
        current_question = self.q[current_question][1]

        return current_question

    def message(self, answer):
        if answer == "yes":
            print("Wohoo! I guessed it! Try again?")
        else:
            print("Oops! Something went wrong! Try again?")