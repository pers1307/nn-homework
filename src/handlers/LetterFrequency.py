import string

class LetterFrequency(object):

    def __init__(self):
        self.words = []
        self.charDictionary = {}

    def calculate(self, text):
        self.countWords(self, text)
        self.charDictionary = {}

        for symbol in text:
            symbol = symbol.lower()

            if (string.ascii_lowercase.find(symbol) == -1):
                continue

            count = self.charDictionary.get(symbol, 'none')

            if (count == 'none'):
                self.charDictionary.update({symbol: 1})
            else:
                self.charDictionary.update({symbol: count + 1})

    def countWords(self, text):
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
        wordCount = self.words.count()





        return '123'