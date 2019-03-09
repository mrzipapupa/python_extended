import csv
import re


def file_parser(fileName):
    with open(fileName, 'r') as file:
        return file.read()


def data_parser(data):
    patternProducer = 'Изготовитель системы:(\s+)(.+)'
    patternOS = 'Название ОС:(\s+)(.+)'
    patternCode = 'Код продукта:(\s+)(.+)'
    patternType = 'Тип системы:(\s+)(.+)'

    result = re.search(patternProducer, data)
    Producer = result.group(2).rstrip()
    result = re.search(patternOS, data)
    OS = result.group(2).rstrip()
    result = re.search(patternCode, data)
    Code = result.group(2).rstrip()
    result = re.search(patternType, data)
    Type = result.group(2).rstrip()

    return {'Producer': Producer, 'OS': OS, 'Code': Code, 'Type': Type}


def get_data():
    mainData = []
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    osProdList = []
    osNameList = []
    osCodeList = []
    osTypeList = []

    for fileNum in range(1,4):
        fileName = 'info_{0}.txt'.format(fileNum)
        fileData = file_parser(fileName)
        fields = data_parser(fileData)
        osProdList.append(fields['Producer'])
        osNameList.append(fields['OS'])
        osCodeList.append(fields['Code'])
        osTypeList.append(fields['Type'])

    mainData.append(headers)
    COUNTFILES = 3

    for num in range(COUNTFILES):
        dataList = []
        dataList.append(osProdList[num])
        dataList.append(osNameList[num])
        dataList.append(osCodeList[num])
        dataList.append(osTypeList[num])
        mainData.append(dataList)

    return mainData

def write_to_csv(CSVfileName):
    dataForFile = get_data()
    with open(CSVfileName, 'w', newline='') as fileCSV:
        writer = csv.writer(fileCSV)
        writer.writerows(dataForFile)


if __name__ == '__main__':
    write_to_csv('report.csv')