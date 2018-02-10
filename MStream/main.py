from MStream import MStream
import json
import time

dataDir = "data/"
outputPath = "result/"

# dataset = "TREC"
# dataset = "TREC-T"
dataset = "News"
# dataset = "News-T"

timefil = "timefil"
MaxBatch = 2 # The number of saved batches + 1
AllBatchNum = 16 # The number of batches you want to devided the dataset to
alpha = 0.03
beta = 0.03
iterNum = 5
sampleNum = 1
wordsInTopicNum = 5
K = 0 


def runMStreamF(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum):
    mstream = MStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    mstream.getDocuments()
    for sampleNo in range(1, sampleNum+1):
        print("SampleNo:"+str(sampleNo))
        mstream.runMStreamF(sampleNo, outputPath)

def runMStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum):
    mstream = MStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    mstream.getDocuments()
    for sampleNo in range(1, sampleNum+1):
        print("SampleNo:"+str(sampleNo))
        mstream.runMStream(sampleNo, outputPath)

def runWithAlphaScale(beta, K, MaxBatch, AllBatchNum, iterNum, sampleNum, dataset, timefil, wordsInTopicNum):
    parameters = []
    timeArrayOfParas = []

    p = 0.01
    while p <= 0.051:
        alpha = p
        parameters.append(p)
        print("alpha:", alpha, "\tp:", p)
        mstream = MStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
        mstream.getDocuments()
        timeArray = []
        for sampleNo in range(1, sampleNum + 1):
            print("SampleNo:", sampleNo)
            startTime = time.time()
            mstream.runMStreamF(sampleNo, outputPath)
            endTime = time.time()
            timeArray.append(int(endTime - startTime))
        timeArrayOfParas.append(timeArray)
        p += 0.001

    fileParameters = "MStreamDiffAlpha" + "K" + str(K) + "iterNum" + str(iterNum) + "SampleNum" + \
                     str(sampleNum) + "beta" + str(round(beta, 3)) + \
                        "BatchNum" + str(AllBatchNum) + "BatchSaved" + str(MaxBatch)
    outTimePath = outputPath + "Time" + dataset + fileParameters + ".txt"
    writer = open(outTimePath, 'w')
    parasNum = parameters.__len__()
    for i in range(parasNum):
        temp_obj = {}
        temp_obj['parameter'] = parameters[i]
        temp_obj['Time'] = timeArrayOfParas[i]
        temp_json = json.dumps(temp_obj)
        writer.write(temp_json)
        writer.write('\n')
    writer.close()

def runWithBetas(alpha, K, MaxBatch, AllBatchNum, iterNum, sampleNum, dataset, timefil, wordsInTopicNum):
    parameters = []
    timeArrayOfParas = []
    beta = 0.01
    while beta <= 0.0501:
        parameters.append(beta)
        print("beta:", beta)
        mstream = MStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
        mstream.getDocuments()
        timeArray = []
        for sampleNo in range(1, sampleNum + 1):
            print("SampleNo:", sampleNo, end=' ')
            startTime = time.time()
            mstream.runMStreamF(sampleNo, outputPath)
            endTime = time.time()
            timeArray.append(int(endTime - startTime))
        timeArrayOfParas.append(timeArray)
        beta += 0.002
    fileParameters = "MStreamDiffBeta" + "K" + str(K) + "iterNum" + str(iterNum) + "SampleNum" + str(sampleNum) + \
                     "alpha" + str(round(alpha, 3)) + \
                        "BatchNum" + str(AllBatchNum) + "BatchSaved" + str(MaxBatch)
    outTimePath = outputPath + "Time" + dataset + fileParameters + ".txt"
    writer = open(outTimePath, 'w')
    parasNum = parameters.__len__()
    for i in range(parasNum):
        temp_obj = {}
        temp_obj['parameter'] = parameters[i]
        temp_obj['Time'] = timeArrayOfParas[i]
        temp_json = json.dumps(temp_obj)
        writer.write(temp_json)
        writer.write('\n')
    writer.close()

def runWithNiters(K, MaxBatch, AllBatchNum, alpha, beta, sampleNum, dataset, timefil, wordsInTopicNum):
    parameters = []
    timeArrayOfParas = []
    iterNum = 0
    while iterNum <= 30.01:
        parameters.append(iterNum)
        print("iterNum:", iterNum)
        mstream = MStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
        mstream.getDocuments()
        timeArray = []
        for sampleNo in range(1, sampleNum + 1):
            print("SampleNo:", sampleNo, end=' ')
            startTime = time.time()
            mstream.runMStreamF(sampleNo, outputPath)
            endTime = time.time()
            timeArray.append(int(endTime - startTime))
        timeArrayOfParas.append(timeArray)
        iterNum += 1
    fileParameters = "MStreamDiffIter" + "K" + str(K) + "SampleNum" + str(sampleNum) + \
                     "alpha" + str(round(alpha, 3)) + "beta" + str(round(beta, 3)) + \
                        "BatchNum" + str(AllBatchNum) + "BatchSaved" + str(MaxBatch)
    outTimePath = outputPath + "Time" + dataset + fileParameters + ".txt"
    writer = open(outTimePath, 'w')
    parasNum = parameters.__len__()
    for i in range(parasNum):
        temp_obj = {}
        temp_obj['parameter'] = parameters[i]
        temp_obj['Time'] = timeArrayOfParas[i]
        temp_json = json.dumps(temp_obj)
        writer.write(temp_json)
        writer.write('\n')
    writer.close()

def runWithBatchNum(K, MaxBatch, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum):
    parameters = []
    timeArrayOfParas = []
    BatchNum = 5
    while BatchNum <= 30.1:
        parameters.append(BatchNum)
        print("BatchNum:", BatchNum)
        mstream = MStream(K, MaxBatch, BatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
        mstream.getDocuments()
        timeArray = []
        for sampleNo in range(1, sampleNum + 1):
            print("SampleNo:", sampleNo, end=' ')
            startTime = time.time()
            mstream.runMStreamF(sampleNo, outputPath)
            endTime = time.time()
            timeArray.append(int(endTime - startTime))
        timeArrayOfParas.append(timeArray)
        BatchNum += 1
    fileParameters = "MStreamDiffBatchNum" + "K" + str(K) + "iterNum" + str(iterNum) + "SampleNum" + str(sampleNum) + \
                     "alpha" + str(round(alpha, 3)) + "beta" + str(round(beta, 3)) + \
                        "BatchNum" + str(AllBatchNum) + "BatchSaved" + str(MaxBatch)
    outTimePath = outputPath + "Time" + dataset + fileParameters + ".txt"
    writer = open(outTimePath, 'w')
    parasNum = parameters.__len__()
    for i in range(parasNum):
        temp_obj = {}
        temp_obj['parameter'] = parameters[i]
        temp_obj['Time'] = timeArrayOfParas[i]
        temp_json = json.dumps(temp_obj)
        writer.write(temp_json)
        writer.write('\n')
    writer.close()

def runWithMaxBatch(K, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum):
    parameters = []
    timeArrayOfParas = []
    MaxBatch = 1
    while MaxBatch <= 16.1:
        parameters.append(MaxBatch)
        print("MaxBatch:", MaxBatch)
        mstream = MStream(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
        mstream.getDocuments()
        timeArray = []
        for sampleNo in range(1, sampleNum + 1):
            print("SampleNo:", sampleNo, end=' ')
            startTime = time.time()
            mstream.runMStreamF(sampleNo, outputPath)
            endTime = time.time()
            timeArray.append(int(endTime - startTime))
        timeArrayOfParas.append(timeArray)
        MaxBatch += 1
    fileParameters = "MStreamDiffMaxBatch" + "K" + str(K) + "iterNum" + str(iterNum) + "SampleNum" + str(sampleNum) + \
                     "alpha" + str(round(alpha, 3)) + "beta" + str(round(beta, 3)) + \
                        "BatchNum" + str(AllBatchNum) + "BatchSaved" + str(MaxBatch)
    outTimePath = outputPath + "Time" + dataset + fileParameters + ".txt"
    writer = open(outTimePath, 'w')
    parasNum = parameters.__len__()
    for i in range(parasNum):
        temp_obj = {}
        temp_obj['parameter'] = parameters[i]
        temp_obj['Time'] = timeArrayOfParas[i]
        temp_json = json.dumps(temp_obj)
        writer.write(temp_json)
        writer.write('\n')
    writer.close()

if __name__ == '__main__':

    runMStream(K, AllBatchNum, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    # runMStreamF(K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    # runWithAlphaScale(beta, K, MaxBatch, AllBatchNum, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    # runWithBetas(alpha, K, MaxBatch, AllBatchNum, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    # runWithNiters(K, MaxBatch, AllBatchNum, alpha, beta, sampleNum, dataset, timefil, wordsInTopicNum)
    # runWithBatchNum(K, MaxBatch, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
    # runWithMaxBatch(K, AllBatchNum, alpha, beta, iterNum, sampleNum, dataset, timefil, wordsInTopicNum)
