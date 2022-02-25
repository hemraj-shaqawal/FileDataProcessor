import logging as logger
import os
import re
from typing import List, Dict, Any
from db.dboperation import dboperation

logger.basicConfig(filename="Log/appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

class controller:

    def __init__(self):
        try:
           self.uniqueWordCollectionWithCount = dict()
           self.finalWordCountList = []
           self.finalAlphaCountList = []
           self.fileList = os.listdir("dataset")
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def filereaderParser(self):
        """create a dict with filedata"""
        try:
            self.fileData = dict()
            for item in self.fileList:
                with open( f'dataset/{item}', "r", encoding="utf8") as f:
                    data = f.readlines()
                    self.fileData[item] = [word.strip('\n') for word in data]
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def getWordFrequency(self):
        """this function willfind out a count of each and every word in a respective file return a list of tuple with word and its respective count
        sample example -  [('sudh', 6 ) , ('kumar',3)]"""
        try:
            self.uniqueWordCollectionWithCount = dict()
            for key,items in self.fileData.items():
                for item in items:
                    item = re.sub(r'[^a-zA-Z]', '', item)
                    d_key = str(item)
                    if d_key in self.uniqueWordCollectionWithCount.keys():
                        self.uniqueWordCollectionWithCount[d_key] = self.uniqueWordCollectionWithCount[d_key] + 1
                    else:
                        self.uniqueWordCollectionWithCount[d_key] = 1
            self.finalWordCountList.append([(k, v) for k, v in self.uniqueWordCollectionWithCount.items()])
            logger.info(self.finalWordCountList)

        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def getWordFrequencyBasedOnAlphabet(self):
        """this function will perform a operation to get a count of all the word starting with same alphabet
                    sample examle = [(a,56) , (b,34),...........]"""
        try:
            self.alphaWordCollectionWithCount = dict()
            for key, items in self.fileData.items():
                for item in items:
                    item = re.sub(r'[^a-zA-Z]', '', item)
                    d_key = str(item)
                    if d_key != None and len(d_key) > 0:
                        firstAlpha = str(d_key[0])

                        if firstAlpha in self.alphaWordCollectionWithCount.keys():
                            self.alphaWordCollectionWithCount[firstAlpha] = self.alphaWordCollectionWithCount[firstAlpha] + 1
                        else:
                            self.alphaWordCollectionWithCount[firstAlpha] = 1

            self.finalAlphaCountList.append([(k, v) for k, v in self.alphaWordCollectionWithCount.items()])
            logger.info(self.finalAlphaCountList)

        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def getAllWordWithSenilizedStr(self):
        """this function will filter out all the words from dataset without number and special char"""
        try:
            self.wordList = set()
            for key, items in self.fileData.items():
                for item in items:
                   wr =  re.sub(r'[^a-zA-Z]', '', item)
                   if wr != None and len(wr) > 0:
                        self.wordList.add(wr)

            self.finalWordList = list(self.wordList)
            logger.info(self.finalWordList)
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def generateTupleSetOfWord(self):
        """this function will filter out all the words from dataset create a tuple of it"""
        try:
            self.wordList = set()
            for key, items in self.fileData.items():
                for item in items:
                    enStr = item.encode(encoding='UTF-8', errors='strict')
                    self.wordList.add(enStr)

            self.finalWordTuple = tuple(self.wordList)
            logger.info(self.finalWordTuple)
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def insertWordINTable(self):
        """This function will insert data from wordCollection table"""
        try:
            self.generateTupleSetOfWord()
            dataSet = [(item.decode('utf-8', 'replace'), )  for item in self.finalWordTuple]
            obj1 = dboperation()
            obj1.insertWordINTable(dataSet)
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def getWordfromTable(self):
        """This function will fetch data from wordCollection table"""
        try:
            obj1 = dboperation()
            res = obj1.getWordFromDB()
            logger.info(res)
        except Exception as e:
            logger.exception("Exception occured" + str(e))