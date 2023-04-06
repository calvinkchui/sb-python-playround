import logging
import logging.config


# Functions
def byCode1():

  # Case 1:
  logging.basicConfig(filename='out/logger.log', level=logging.INFO)
  logging.debug('debug message')
  logging.info('info message')
  logging.warn('warn message')
  logging.error('error message')
  logging.critical('critical message V1')


def byCode2():

  # Case 2:
  logger_name = "example"
  logger = logging.getLogger(logger_name)
  logger.setLevel(logging.DEBUG)

  # create file handler
  log_path = "out/logger.log"
  fh = logging.FileHandler(log_path)
  fh.setLevel(logging.WARN)

  # create formatter
  fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
  datefmt = "%a %d %b %Y %H:%M:%S"
  formatter = logging.Formatter(fmt, datefmt)

  # add handler and formatter to logger
  fh.setFormatter(formatter)
  logger.addHandler(fh)

  logger.debug('debug message #2')
  logger.info('info message #2')
  logger.warn('warn message #2')
  logger.error('error message #2')
  logger.critical('critical message #2')


def byConf():

  logging.config.fileConfig("./logging.conf")

  logger_name = "example01"
  logger = logging.getLogger(logger_name)

  logger.debug('debug message #Cfg')
  logger.info('info message #Cfg')
  logger.warn('warn message #Cfg')
  logger.error('error message #Cfg')
  logger.critical('critical message #Cfg')


byCode1()
byCode2()
byConf()
