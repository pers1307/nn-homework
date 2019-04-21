from src.services.StatisticTextService import StatisticTextService
from src.handlers.AverageSentenceLength import AverageSentenceLength
from src.handlers.AverageWordLength import AverageWordLength
from src.handlers.LetterFrequency import LetterFrequency

pathToTextFile = 'data/longEnglishText.txt'
pathToOutFile = 'data/statisticEnglishText.txt'

statisticTextService = StatisticTextService()

statisticTextService.addHandler(AverageSentenceLength)
statisticTextService.addHandler(AverageWordLength)
statisticTextService.addHandler(LetterFrequency)

statisticTextService.calculate(pathToTextFile)
statisticTextService.saveResult(pathToOutFile)