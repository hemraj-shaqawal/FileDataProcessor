"""Task for today : dataset - https://archive.ics.uci.edu/ml/datasets/Bag+of+Words

q1 = try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count
   sample example -  [('sudh', 6 ) , ('kumar',3)]

q2 = try to perform a reduce operation to get a count of all the word starting with same alphabet
    sample examle = [(a,56) , (b,34),...........]

q3 = Try to filter out all the words from dataset .

.001.abstract = abstract
=.002 = delete

q4 = create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB .
(aah,>=,354,fdsf,wer)

Top 10 will be able to get kids neuron

"""

import logging as logger
from controller.controller import  controller
from db.dboperation import dboperation
logger.basicConfig(filename="Log/appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

if __name__ == '__main__':
    "Note for output Please check"
    logger.info("App started sucessfully!")
    obj = controller()
    obj.filereaderParser()

    while True:
        inp = eval(input(
            "press 1 for get Word Frequency. press 2 for get Word Frequency Based On Alphabet. press 3 for get All Word With Senitized String. press 4 for insert Word In Table. press 5 for get word form table, press 6 for exit => "))
        if (type(inp) == int and inp == 1):
            obj.getWordFrequency()
            break
        elif (type(inp) == int and inp == 2):
            obj.getWordFrequencyBasedOnAlphabet()
            break
        elif (type(inp) == int and inp == 3):
            obj.getAllWordWithSenilizedStr()
            break
        elif (type(inp) == int and inp == 4):
            obj.insertWordINTable()
            break
        elif (type(inp) == int and inp == 5):
            obj.getWordfromTable()
            break
        elif (type(inp) == int and inp == 6):
            """This is option for exit"""
            break
        else:
            logger.info("Please enter a valid input!")


