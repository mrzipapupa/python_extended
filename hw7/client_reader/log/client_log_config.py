import logging
import os

loggerInfo = logging.getLogger('client.info')
loggerError = logging.getLogger('client.errors')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

fhInfo = logging.FileHandler(os.path.join('.\\log', 'client_info.log'), encoding='utf-8')
fhInfo.setLevel(logging.DEBUG)
fhInfo.setFormatter(formatter)

fhError = logging.FileHandler(os.path.join('.\\log', 'client_errors.log'), encoding='utf-8')
fhError.setLevel(logging.WARNING)
fhError.setFormatter(formatter)

loggerInfo.addHandler(fhInfo)
loggerInfo.setLevel(logging.DEBUG)
loggerError.addHandler(fhError)
loggerError.setLevel(logging.WARNING)


if __name__ == '__main__':
    pass