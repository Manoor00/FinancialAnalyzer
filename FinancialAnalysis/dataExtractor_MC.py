# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:50:46 2017

@author: Shark
"""
from urllib.request import urlopen
import time
#import mongo

class moneyControl:
    def __init__(self):
        self.baseUrl = "http://www.moneycontrol.com/india/stockpricequote/"
        self.Extractors = {}
        self.Extractors["companyListExtractorStart"] = "<strong>Company Name</strong>"
        self.Extractors["companyListExtractorEnd"] = "Moneycontrol Footer start here"
        self.Extractors["companyQuoteStart"]       = "\"Bse_Prc_tick\"><strong>" 
        self.Extractors["companyQuoteEnd"]         = "</strong>"
        self.Extractors["companyNameStart"]  = "<input type=\"hidden\" name=\"compname_imp\" id=\"compname_imp\" value=\""
        self.Extractors["companyNameEnd"]    = "\">"
        self.Extractors["companyKeyStart"]  = "<input type=\"hidden\" name=\"compid_imp\" id=\"compid_imp\" value=\""
        self.Extractors["companyKeyEnd"]    = "\">"
        self.companyUrlList = []
        self.companyMap = {};
        self.numIt = 0
        self.sleep = 1
        self.configuredCompanyList = []
        self.readCompanyListFromConfig()
        
    def readCompanyListFromConfig(self):
        configFile = open("CompanyList.txt", "r")
        for line in configFile:
            self.configuredCompanyList.append(line.strip())
        
        
    def GetCompanyInConfig(self, url):
        for company in self.configuredCompanyList:
            if company in url:
                return True
        return False
    
    def extract(self,inputStr,start, end):
        index = inputStr.find(start) + len(start)
        index2 = inputStr[index:].find(end)
        tempStr = inputStr[index:index+index2]
        return tempStr
        
    def getCompaniesList(self, fromConfig = False):
        html = urlopen(self.baseUrl).read().decode('utf-8')
        index_start = 0
        index_start = html.find(self.Extractors["companyListExtractorStart"])
        index_end = html.find(self.Extractors["companyListExtractorEnd"]);
        Company_list = html[index_start:index_end]
        Company_list = Company_list.replace("\t","")
        Company_listArray = Company_list.split("\r\n")

        for i , elem in enumerate(Company_listArray):
            if(elem.find("a href") != -1):
                sub = elem[9:elem.find("\" title")]
                #print(sub)
                if fromConfig == False or self.GetCompanyInConfig(sub) == True:
                    self.companyUrlList.append(sub)
        self.numIt = len(self.companyUrlList)
        return
    
    def extractQuotes(self):
        #db = dbWrapper("mongodb+srv://shark:whirlpool$1@stocks-jnw5u.mongodb.net/test")
        companyList = []
        for i , elem in enumerate( self.companyUrlList):
            try:
                html = urlopen(elem).read().decode('utf-8')
            except UnicodeDecodeError as e:
                print("Exception in {}".format(e.start))
                try:
                    html = urlopen(elem).read(e.start).decode('utf-8')
                except UnicodeDecodeError as e:
                    print("exception in {}", elem)
                    continue
            except Exception:
                print("Exception in {}".format(elem))
                
            cInfo = CInfo()

            cInfo.industry = self.extract(elem, "stockpricequote/","/")
            print("industry = {}".format(cInfo.industry))
            
            cInfo.quote = float(self.extract(html, obj.Extractors["companyQuoteStart"], obj.Extractors["companyQuoteEnd"]))
            print("quote = {}".format(cInfo.quote))
            
            cInfo.name = self.extract(html, obj.Extractors["companyNameStart"], obj.Extractors["companyNameEnd"])
            print("name = {}".format(cInfo.name))
            
            cInfo.key = self.extract(html, obj.Extractors["companyKeyStart"], obj.Extractors["companyKeyEnd"])
            print("key = {}".format(cInfo.key))
            
            try:
                cInfo.yrLow = float(self.extract(html, "id=\"b_52low\">", "</"))
                print("52Week Low = {}".format(cInfo.yrLow))
            except ValueError:
                print("exception")
            
            try:
                cInfo.yrHigh = float(self.extract(html, "id=\"b_52high\">", "</"))
                print("52Week High = {}".format(cInfo.yrHigh))
            except ValueError:
                print("exception")
            
            temp = html.find("Consolidated data starts here")
            
            try:
                tempStr = self.extract(html[temp:], "<div class=\"FL gL_10 UC\">P/E</div>", "class=\"CL\"")
                cInfo.pe = float(self.extract(tempStr, "<div class=\"FR gD_12\">", "</"))
                print("P/E = {}".format(cInfo.pe))
            except ValueError:
                print("exception")
            
            try:
                tempStr = self.extract(html[temp:], "<div class=\"FL gL_10 UC\">INDUSTRY P/E</div>", "class=\"CL\"")
                cInfo.industryPE = float(self.extract(tempStr, "<div class=\"FR gD_12\">", "</"))
                print("Industry P/E = {}".format(cInfo.industryPE))
            except ValueError:
                print("exception")
                
            
            temp = html.find("<strong>Simple Moving Averages</strong>")
            
            try:
                tempStr = self.extract(html[temp:], "<td class=\"th05 gD_12\">30</td>", "class=\"th06")
                cInfo.movingAvg['30'] = float(self.extract(tempStr, "<td class=\"th05 gD_12\">", "</"))
                print("30 day moving average = {}".format(cInfo.movingAvg['30']))
                
                tempStr = self.extract(html[temp:], "<td class=\"th05 gD_12\">50</td>", "class=\"th06")
                cInfo.movingAvg['50'] = float(self.extract(tempStr, "<td class=\"th05 gD_12\">", "</"))
                print("50 day moving average = {}".format(cInfo.movingAvg['50']))
                
                tempStr = self.extract(html[temp:], "<td class=\"th05 gD_12\">150</td>", "class=\"th06")
                cInfo.movingAvg['150'] = float(self.extract(tempStr, "<td class=\"th05 gD_12\">", "</"))
                print("150 day moving average = {}".format(cInfo.movingAvg['150']))
                
                tempStr = self.extract(html[temp:], "<td class=\"th05 gD_12\">200</td>", "class=\"th06")
                cInfo.movingAvg['200'] = float(self.extract(tempStr, "<td class=\"th05 gD_12\">", "</"))
                print("200 day moving average = {}".format(cInfo.movingAvg['200']))
            except ValueError:
                print("exception")
                
            #row = {"Stock":cInfo.toJson()}
            #print(row)

            #db.insertRow(row);
            
            if(i>self.numIt):
                break;
            companyList.append(cInfo)                
            time.sleep(self.sleep)

        return companyList