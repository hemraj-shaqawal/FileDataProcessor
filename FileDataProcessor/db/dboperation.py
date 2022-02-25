import logging as logger
import sqlite3

logger.basicConfig(filename="Log/appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

class dboperation:

    def __init__(self):
        try:
            self.createTable()
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def getConnection(self):
        try:
            db = sqlite3.connect("myApp.db")
            return db
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def createTable(self):
        """This function will create a table in db """
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='wordCollection' ''')

            # if the count is 1, then table exists
            if cursor.fetchone()[0] == 1:
                logger.info('Table exists!')
            else:
                logger.info('Table does not exist.')
                cursor.execute("create table wordCollection(id INTEGER PRIMARY KEY, rewordTxt text)")
                connection.commit()
                cursor.close()
                connection.close()
        except Exception as e:
            logger.exception("Exception occured" + str(e))


    def insertWordINTable(self,dataset):
        """This function will insert data into table"""
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            response = cursor.executemany("insert into wordCollection(rewordTxt) values (?)", dataset)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            logger.exception("Exception occured" + str(e))

    def getWordFromDB(self):
        """This function will fetch data from wordCollection table"""
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            data = cursor.execute("select * from wordCollection limit 50")
            response = [i for i in data]
            cursor.close()
            connection.close()
            return response
        except Exception as e:
            logger.exception("Exception occured" + str(e))