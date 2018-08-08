# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:07:39 2017

@author: Shark
"""
import dataExtractor_MC
import MySqlWrapper
#import mongo


obj = moneyControl()
obj.getCompaniesList(True)
'''
http://www.moneycontrol.com/india/stockpricequote/banksprivatesector/yesbank/YB
http://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI
http://www.moneycontrol.com/india/stockpricequote/computerssoftware/tataconsultancyservices/TCS
http://www.moneycontrol.com/india/stockpricequote/financehousing/housingdevelopmentfinancecorporation/HDF
http://www.moneycontrol.com/india/stockpricequote/banksprivatesector/hdfcbank/HDF01
http://www.moneycontrol.com/india/stockpricequote/personalcare/hindustanunilever/HU
http://www.moneycontrol.com/india/stockpricequote/banksprivatesector/icicibank/ICI02
http://www.moneycontrol.com/india/stockpricequote/computerssoftware/infosys/IT
http://www.moneycontrol.com/india/stockpricequote/transportlogistics/interglobeaviation/IA04
http://www.moneycontrol.com/india/stockpricequote/cigarettes/itc/ITC
http://www.moneycontrol.com/india/stockpricequote/banksprivatesector/kotakmahindrabank/KMB
http://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/larsentoubro/LT
http://www.moneycontrol.com/india/stockpricequote/autocarsjeeps/marutisuzukiindia/MS24
http://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/oilnaturalgascorporation/ONG
http://www.moneycontrol.com/india/stockpricequote/bankspublicsector/statebankindia/SBI
http://www.moneycontrol.com/india/stockpricequote/oil-drilling-and-exploration/gailindia/GAI
http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/axisbank/AB16
http://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/aurobindopharma/AP
http://www.moneycontrol.com/india/stockpricequote/trading/urjaglobal/UG01
http://www.moneycontrol.com/india/stockpricequote/personal-care/jhssvendgaardlaboratories/JHS01
'''
#obj.numIt = 1
#obj.sleep = 10

print(len(obj.companyUrlList))

#print(obj.companyUrlList)
headerToValue = {}
companyList = obj.extractQuotes()
mysqlWrapper = MySqlWrapper.MySqlWrapper(headerToValue)

for company in companyList:
    add_elem, data_element = company.toMysqlStatement()
    print(add_elem, data_element)
    mysqlWrapper.InsertDataIntoDb2(add_elem, data_element)