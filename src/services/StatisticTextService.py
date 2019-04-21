# После обработки передаем путь к выходному файлу где все сохраняется
# Потом по запросу отдают результат и он записывается в файл

class StatisticTextService(object):

    def __init__(self):
        self.handlers = []

    def addHandler(self, handler):
        self.handlers.append(handler)

    def calculate(self, pathToFile):
        with open(pathToFile, 'r') as file:
            text = file.read()

        for handler in self.handlers:
            handler.calculate(text)

    def saveResult(self, pathToFile):
        pass