import json
from Document import Document

class DocumentSet:

    def __init__(self, dataDir, wordToIdMap, wordList):
        self.D = 0  # The number of documents
        # self.clusterNoArray = []
        self.documents = []
        with open(dataDir) as input:
            line = input.readline()
            while line:
                self.D += 1
                obj = json.loads(line)
                text = obj['textCleaned']
                document = Document(text, wordToIdMap, wordList, int(obj['tweetId']))
                self.documents.append(document)
                line = input.readline()
        print("number of documents is ", self.D)