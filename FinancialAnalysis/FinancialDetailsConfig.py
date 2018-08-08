# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:22:27 2018

@author: smanoor
"""

import logging

ConfigFileName = "FinancialDetailsConfig"
headerStr = "Headers_"
dataStr = "Data_"
formulaStr = "Formula_"
mainHeader = "Headers_Main"

class ConfigFile:
    def __init__(self):    
        self.configFile = open(ConfigFileName, "r")
        self.mainHeaders = []
        self.headers = {}
        self.data = {}
        self.formula = {}
        self.parseConfigFile()
        #self.printConfig()
        
    def printConfig(self):
        print("-----------------MainHeader-------------")
        for value in self.mainHeaders:
            print(value)

        print("-----------------Header-------------")
        for key in self.headers:
            print(key,"=", self.headers[key])
            
        print("-----------------Formula-------------")
        for key in self.formula:
            print(key,"=", self.formula[key])
            
        print("-----------------Data-------------")
        for key in self.data:
            print(key,"=", self.data[key])
    
    def parseConfigFile(self):
        for line in self.configFile:
            line = line.strip()
            if line != "":
                avp = line.split("=")
                
                if mainHeader in avp[0]:
                    values = avp[1].split(",")
                    for value in values:
                        self.mainHeaders.append(value.strip())
                        
                if headerStr in avp[0]:
                    values = avp[1].split(",")           
                    tempList = []
                    for value in values:
                        tempList.append(value.strip())
                    self.headers[avp[0].strip()] = tempList
                
                if formulaStr in avp[0]:
                    values = avp[1].split(",")           
                    tempList = []
                    for value in values:
                        tempList.append(value.strip())
                    self.formula[avp[0].strip()] = tempList
                
                if dataStr in avp[0]:
                    values = avp[1].split(",")           
                    self.data[avp[0].strip()] = avp[1].strip()
                    

if __name__ == "__main__":
    logger = logging.getLogger('FinancialDetailsConfig')
    hdlr = logging.FileHandler('FinancialDetailsConfig.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    logger.info("starting")
    configFile = ConfigFile()
    