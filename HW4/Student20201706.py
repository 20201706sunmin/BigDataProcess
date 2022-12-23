import numpy as np
import os
import sys
import operator
 
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
    
  
def DataToArray(filename):
    returnMat = np.zeros((1, 1024)) #글자수
    f = open(filename)
    for i in range(32): #32행
        line = f.readline()
        for j in range(32): #32열
            returnMat[0, 32*i+j] = int(line[j])
    return returnMat

trainingDigitsList = os.listdir(sys.argv[1]) 
testDigitsList = os.listdir(sys.argv[2])

trainingDataSize = len(trainingDigitsList) #1934
testDataSize = len(testDigitsList)

trainingMat = np.zeros((trainingDataSize, 1024)) #1934 * 1024

labels = []
for i in range(trainingDataSize):
	filename = trainingDigitsList[i].split('.')[0]
	number = int(filename.split('_')[0])
	labels.append(number)
	trainingMat[i, :] = DataToArray('trainingDigits/%s' % trainingDigitsList[i])


for j in range(1, 21):
	count = 0
	errorRate = 0
	for i in range(testDataSize):
		filename = testDigitsList[i].split('.')[0]
		number = int(filename.split('_')[0])
		testData = DataToArray('testDigits/%s' % testDigitsList[i])		
		result = classify0(testData, trainingMat, labels, j)
		
		#print(result)
		if result != number :
			count += 1

	errorRate = int(count / testDataSize * 100)
	print(errorRate)
