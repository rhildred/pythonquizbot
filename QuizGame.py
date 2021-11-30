class Question:
    def __init__(self, question, answera, answerb, answerc, answerd, correct):
        self.__question = question
        self.__answers = [answera, answerb, answerc, answerd]
        self.__correct = correct
    def ask(self):
        aChoices = []
        aChoices.append(self.__question)
        for n in range(0, 4):
            aChoices.append("   " + str(n + 1) + ")" +  self.__answers[n])
        return aChoices
    def answer(self):
        return self.__correct
                  
class QuizGame:
    def __init__(self):
        self.__current = 0
        self.__nCorrect = 0
        self.__questions = [
            Question("What color is the sky?", "blue", "yellow", "diamond",
                     "purple", 1),
            Question("Which planet is third from the sun?", "Pluto", "Jupiter", "Mercury", "Earth", 4)
        ]
    def takeTurn(self, sInput):
        aReturn = []
        if self.__current == 0:
            self.__current = 1
            aReturn.append("this is a quiz game")
            aReturn += self.__questions[0].ask()
        else:
            try:
                if int(sInput) == self.__questions[self.__current - 1].answer():
                    aReturn.append("correct")
                    self.__nCorrect += 1
                else:
                    aReturn.append("incorrect")
                try:
                    aReturn += self.__questions[self.__current].ask()
                    self.__current += 1
                except:
                    aReturn.append("Thank-you for playing")
                    aReturn.append("You got " + str(self.__nCorrect) + " correct.")
                    self.__current = 0
            except:
                aReturn.append("please choose a number")
        return aReturn

if __name__ == '__main__':
    oGame = QuizGame()

    while True:
        sInput = input("> ")
        aReturn = oGame.takeTurn(sInput)
        for line in aReturn:
            print(line)
