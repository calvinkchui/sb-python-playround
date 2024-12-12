from loguru import logger


def case01():
    logger.debug("01 - default - That's it, beautiful and simple logging!") # system out
'''
2024-12-11 23:29:37.334 | DEBUG    | advance.loguru:case01:5 - 01 - default - That's it, beautiful and simple logging!
'''
def case02_fileout():
    logger.add("tmp/loguru_out_{time}.log")
    logger.debug("02 - fileout - That's it, beautiful and simple logging!") # system out
'''
2024-12-11 23:29:37.348 | DEBUG    | advance.loguru:case02_fileout:9 - 02 - fileout - That's it, beautiful and simple logging!
'''

def demo():
    case01()
    case02_fileout()