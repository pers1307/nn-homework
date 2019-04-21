class StatisticTextService(object):

    def __init__(self):
        self.handlers = []

    def addHandler(self, handler):
        self.handlers.append(handler)

    def calculate(self, pathToFile):
        with open(pathToFile, 'r') as file:
            text = file.read()

        for handler in self.handlers:
            handler.calculate(handler, text)

    def saveResult(self, pathToFile):
        file = open(pathToFile, 'w')

        for handler in self.handlers:
            file.write(handler.resultAsText(handler) + '\n')

        file.close()