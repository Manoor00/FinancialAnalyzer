# -*- coding: utf-8 -*-
from datetime import date

class CInfo:
    def __init__(self):
        self.key = ""
        self.name = ""
        self.date = date.today().isoformat()
        self.quote = 0.0
        self.pe = 0.0
        self.industry = ""
        self.yrHigh = 0.0
        self.yrLow = 0.0
        self.industryPE = 0.0
        self.movingAvg = {}
        
    def toJson(self):
        row = {'key':self.key, 'Date':self.date,'name':self.name, 'quote':float(self.quote), 'industry':self.industry,
               'pe':self.pe, 'industryPE':self.industryPE, '52 week High':self.yrHigh, '52 Week Low': self.yrLow, 
               'MovingAverage':self.movingAvg}
        return row
    
    def toMysqlStatement(self):
        date = datetime.datetime.now().date()
        add_entry = ("INSERT INTO shares "
             "(`key`, time_inserted, name, quote, pe, industry, industryPe,  yrHigh, yrLow, MA200, MA150, MA50, MA30) "
               "VALUES (%(`key`)s,  %(time_inserted)s, %(name)s, %(quote)s, %(pe)s, %(industry)s, %(industryPe)s, %(yrHigh)s, %(yrLow)s, %(MA200)s, %(MA150)s, %(MA50)s, %(MA30)s )")
        data_entry = {
                    '`key`':self.key, 
                    'time_inserted':date,
                    'name':self.name, 
                    'quote':self.quote, 
                    'pe':self.pe, 
                    'industry':self.industry,
                    'industryPe':self.industryPE, 
                    'yrHigh':self.yrHigh,
                    'yrLow': self.yrLow, 
                    'MA200':self.movingAvg['200'],
                    'MA150':self.movingAvg['150'],
                    'MA50':self.movingAvg['50'],
                    'MA30':self.movingAvg['30']
                    }
        return add_entry, data_entry

def main():
    cInfo = CInfo()
    print(cInfo.date) 
if __name__ == "__main__":
    # execute only if run as a script
    main()