#__author__=='qustl_000'
# -*- coding: utf-8 -*-
# ？？？编程规范，功能说明、时间、作者、注释增强可读性
import numpy as np
import Function

fileName = "1.txt"
trainingData, testData=Function.loadData(fileName)

trainingCharacter,trainingLabel=Function.splitData(trainingData)
testCharacter,testLabel=Function.splitData(testData)

diff1=np.tile(testCharacter[0],(len(trainingCharacter),1))-trainingCharacter
print('测试数据集的一条数据，扩充到与训练数据集同维：')
print(np.tile(testCharacter[0],(len(trainingCharacter),1)))
print('训练数据集：')
print(trainingCharacter)
print('作差后的结果：')
print(diff1)