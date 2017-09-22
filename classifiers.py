"""
Algorithm implementations for Classification
"""
from math import *
import random




def dist(x, y) :
    #function that returns the euclidian distance
    square_Dist = 0

    for i in range(len(x)-1):
        square_Dist += (int(x[i]) - int(y[i]))**2
    #print square_Dist
    return sqrt(square_Dist)



def votingScheme(testData, knn) :
    p_pos = 0
    p_neg = 0
    for data in knn:
        #print data[0][-1]
        if data[0][-1] == '+1' or data[0][-1]=='1':
            p_pos += 1/(1 + data[1])
        #    print "u r in the if statemenet"
        else:
            p_neg += 1/(1+data[1])
    #print ("p_pos = %d; p_neg = %d\n", (p_pos, p_neg))
    if p_pos > p_neg:
        return 1
    return -1


def kNearestNeighbours(trainingData, testData, k):
    #shhhhhhhhh
    test_predictions =[]
    for datapoint in testData:
        distances = []
        for j in range(len(trainingData)):
            #print trainingData[j]
            #print datapoint
            distances.append((trainingData[j], dist(trainingData[j], datapoint)))
        sorted_dists = sorted(distances, key=lambda x: x[1])
        knn = sorted_dists[:k]
        pair = (datapoint, votingScheme(datapoint, knn))
        #print pair
        test_predictions.append(pair)
    #print test_predictions
    return test_predictions




def generateFolds(numFolds, origData):
  indexList = [] #list of numbers from 0 to N-1
  for i in range(len(origData)):
      indexList.append(i)
  random.shuffle(indexList) #list of integers all shuffled up

  shuffledData = [] #empty list
  for index in indexList:
     shuffledData.append(origData[index]) #to shuffledData #this rearranges the rows

  foldSize = len(origData)/float(numFolds) #use float division
  testFold = []
  trainFold = []
  for y in range(numFolds):
    #print y
    #print foldSize
    #print shuffledData
    leftEnd = int(y*foldSize) #this needs to be int (round down)
    rightEnd = int((y+1)*foldSize) #this needs to be an int (round down)
    testFold.append(shuffledData[leftEnd:rightEnd])
    trainFold.append(shuffledData[:leftEnd] + shuffledData[rightEnd:])#rest of shuffledData #items before left end and after right end
    #print testFold
    #print trainFold
  return [trainFold, testFold]
