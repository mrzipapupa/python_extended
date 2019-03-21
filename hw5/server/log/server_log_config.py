import logging
from logging import handlers
import os

loggerInfo = logging.getLogger('server.info')
loggerError = logging.getLogger('server.errors')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

fhInfo = logging.handlers.TimedRotatingFileHandler(os.path.join('.\\log', 'server_info.log'),
                                                   encoding='utf-8', when='D')
fhInfo.setLevel(logging.DEBUG)
fhInfo.setFormatter(formatter)

fhError = logging.handlers.TimedRotatingFileHandler(os.path.join('.\\log', 'server_errors.log'),
                                                    encoding='utf-8', when='D')
fhError.setLevel(logging.WARNING)
fhError.setFormatter(formatter)


loggerInfo.addHandler(fhInfo)
loggerInfo.setLevel(logging.DEBUG)

loggerError.addHandler(fhError)
loggerError.setLevel(logging.DEBUG)


if __name__ == '__main__':
    pass