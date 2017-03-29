import csv

class csvController():
    def __init__(self, fileName):
        self.fileName = fileName

    def readCsv(self):
        csvData = []
        firstLine = True
        with open(self.fileName, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if(len(row) > 0):
                    if(firstLine):
                       titleData = row
                       firstLine = False
                    else:
                        csvData.append(row)

        f.close()
        return titleData, csvData

    def extractColumn(self, dataSet,columnNumber):
        extractedColumn = []
        for counter in range(len(dataSet)):
            extractedColumn.append(dataSet[counter][columnNumber])

        return extractedColumn

    def deleteColumn(self, dataSet, columnNumber):
        for counter in range(len(dataSet)):
            dataSet[counter].remove(dataSet[counter][columnNumber])
        return dataSet

    def convertToFloat(self, dataSet, columnNumer= None):
        if(columnNumer == None):
            for counter in range(len(dataSet)):
                for j in range(len(dataSet[counter])):
                    try:
                        dataSet[counter][j] = float(dataSet[counter][j])
                    except ValueError:
                        print("Error Converting Data set to Float, Err number 1\n", ValueError.args)
        else:
            for counter in range(len(dataSet)):
                try:
                    dataSet[counter][columnNumer] = float(dataSet[counter][columnNumer])
                except ValueError:
                    print("Error Converting Data set to Float, Err number 2\n", ValueError.args)
        return dataSet