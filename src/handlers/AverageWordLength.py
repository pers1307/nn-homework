import numpy as np

class AverageWordLength(object):

    def __init__(self):
        self.words = []

    def calculate(self, text):
        countCharInWord = 0
        self.words = []

        for symbol in text:
            countCharInWord += 1

            if symbol == ' ':
                self.words.append(countCharInWord - 1)
                countCharInWord = 0

        if (countCharInWord != 0):
            self.words.append(countCharInWord)

    def resultAsText(self):
        return 'Средняя длинна слова в буквах: ' + str(np.mean(self.words))