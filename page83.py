import random
def getAnswer(answerNumber):
   if answerNumber == 1:
        return 'It is certain1'
   if answerNumber == 2:
        return 'It is certain2'
   if answerNumber == 3:
        return 'It is certain3'
   if answerNumber == 4:
        return 'It is certain4'
   if answerNumber == 5:
        return 'It is certain5'
   if answerNumber == 6:
        return 'It is certain6'
   if answerNumber == 7:
        return 'It is certain7'
   if answerNumber == 8:
        return 'It is certain8'
   if answerNumber == 9:
        return 'It is certain9'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
