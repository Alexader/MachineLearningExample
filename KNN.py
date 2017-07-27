# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:16:47 2017

@author: LUC
"""
import numpy as np
import operator
def createDataset():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
#get information about data candidate,like whether they paly games,eat icecream
def file2Matrix(fileNmae):
    file = open(fileNmae)
    arrayLines = file.readlines()
    numberofLines = len(arrayLines)
    returnMat = np.zeros((numberofLines,3))
    classLabelVector = []
    index = 0
    for line in arrayLines:
        line = line.strip()
        listFromLines = line.split('\t')
        returnMat[index,:] = listFromLines[0:3]
        classLabelVector.append(int(listFromLines[-1]))
        index += 1
    return returnMat,classLabelVector
def classify0(inX,dataSet,labels,k):
    #calculate the distance of input data to every data in dataset
    dataSize = dataSet.shape[0]#get the number of rows
    diffMat = np.tile(inX,(dataSize,1)) - dataSet
    sqdiffMat = diffMat**2
    sqDistance = sqdiffMat.sum(axis = 1)
    distance = sqDistance**0.5
    #get the index of nearst k datas
    sortedDistanceIndices = distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistanceIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print(type(distance))
    return sortedClassCount[0][0]

group, labels = createDataset()
classify0([0,0],group,labels,3)
out = classify0([0,0],group,labels,3)
print(out)
