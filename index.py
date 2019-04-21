from src.services.StatisticTextService import StatisticTextService
from src.handlers.AverageSentenceLength import AverageSentenceLength
from src.handlers.AverageWordLength import AverageWordLength
from src.handlers.LetterFrequency import LetterFrequency

pathToTextFile = ''
pathToOutFile = ''

statisticTextService = StatisticTextService()

statisticTextService.addHandler(AverageSentenceLength)
statisticTextService.addHandler(AverageWordLength)
statisticTextService.addHandler(LetterFrequency)

statisticTextService.calculate(pathToTextFile)
statisticTextService.saveResult(pathToOutFile)


# Путь к файлу бросаем в класс
# После обработки передаем путь к выходному файлу где все сохраняется
# В сервисе который всем этим рулит нужен класс для загрузки текста

# Класс аккумулирет в себе классы, которые принимают текст, читают что нужно и держат результат
# Потом по запросу отдают результат и он записывается в файл

# todo: пишем класс который загружает текст