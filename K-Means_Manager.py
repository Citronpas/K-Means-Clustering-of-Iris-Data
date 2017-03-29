import numpy as np
import csv
import numpy as np
from scipy.cluster.vq import *
from Clustering import cluster
from CsvController import csvController
from Clustering import ClusterManager
fileName = "D:\PyProjects\PythonProjects\AIForHumVol01\Chapter2\iris.csv"

k=3
csvFile = csvController(fileName)
csvTitles, csvData = csvController.readCsv(csvFile)
extractedColumn = csvController.extractColumn(csvFile, csvData, 4)
csvData = csvController.deleteColumn(csvFile, csvData, 4)

csvData = csvController.convertToFloat(csvFile, csvData)

clustering = ClusterManager(csvData, k)
clustering.randomKMeansInitialization()
Done = False

while Done == False:
    clustering.randomKMeansUpdate()
    Done = clustering.assignmentKMean()
# clustering.printClusters()

a = clustering.getClusters()
print(a[1].getObservation())



# res, idx = kmeans2(np.array(csvData), k)
#
# for cluster in range(0, k):
#     print("Cluster number", str(cluster +1))
#     for i in range(0, len(idx)):
#         if(idx[i] == cluster):
#             print(str(csvData[i]), ",", extractedColumn[cluster])
