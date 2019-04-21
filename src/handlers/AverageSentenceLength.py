import numpy as np

class AverageSentenceLength(object):

    def __init__(self):
        self.sentences = []

    def calculate(self, text):
        countCharInSentence = 0
        self.sentences = []

        for symbol in text:
            countCharInSentence += 1

            if symbol == '.':
                self.sentences.append(countCharInSentence)
                countCharInSentence = 0

        if (countCharInSentence != 0):
            self.sentences.append(countCharInSentence)

    def resultAsText(self):
        return 'Средняя длинна предложения в буквах: ' + str(np.mean(self.sentences))