# -*- coding: utf-8 -*-

import mysql.connector
import datetime

class MySqlWrapper:

    def __init__(self, dataDictionary):
        self.cnx = mysql.connector.connect(user='root', password='Samsung$1',
                              host='35.200.223.120',
                              database='Stocks')
        self.cursor = self.cnx.cursor()
        self.data = dataDictionary
    
    def InsertDataIntoDb(self):
        date = datetime.datetime.now().date()
        for key in self.data:
            print(key, self.data[key])
            add_entry = ("INSERT INTO entries "
             "(time_inserted, name, value_double) "
               "VALUES (%(time_inserted)s, %(name)s, %(value_double)s)")
            data_entry = {
                    'time_inserted': date,
                    'name' : key,
                    'value_double': self.data[key]
                    }
            self.cursor.execute(add_entry, data_entry)

        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

      
    def InsertDataIntoDb2(self, statement, data):
        self.cursor = self.cnx.cursor()
        self.cursor.execute(statement, data)
        self.cnx.commit()
        self.cursor.close()

