# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:16:56 2020

@author: Arnauld
"""

import pandas as pd
import xlrd
import openpyxl

#Sheet 1
Sheet1 = pd.read_excel('Book1.xlsx', sheet_name = 'Sheet1', header = 0)
print(Sheet1)
Sheet1.to_csv('Sheet1.csv', sep='!')
#Sheet 2
Book1_2 = pd.ExcelFile('Book1.xlsx')
Sheet2 = Book1_2.parse(sheet_name = 'Sheet2')
print(Sheet2)
Sheet2.to_csv('Sheet2.csv',sep='*')
#Sheet 3
Sheet3 = pd.read_excel('Book1.xlsx', sheet_name = 'Sheet3', header = 0)
print(Sheet3)
Sheet3.to_csv('Sheet3.csv', sep='!')
#Sheet 4
Sheet4 = Book1_2.parse(sheet_name = 'Sheet4')
print(Sheet4)
Sheet4.to_csv('Sheet4.csv',sep=',')
#Sheet 5
Sheet5 = pd.read_excel('Book1.xlsx', sheet_name = 'Sheet5', header = None)
print(Sheet5)
Sheet1.to_csv('Sheet5.csv', sep='-')


#Sheet 6
Book1_2 = pd.ExcelFile('Book1.xlsx')
Sheet6 = Book1_2.parse(sheet_name = 'Sheet6')
print(Sheet6)
Sheet6.to_csv('Sheet6.csv',sep='*')
#Sheet 7
Sheet7 = pd.read_excel('Book1.xlsx', sheet_name = 'Sheet7', header = 0)
print(Sheet7)
Sheet7.to_csv('Sheet7.csv', sep='!')
#Sheet 8
Book1_2 = pd.ExcelFile('Book1.xlsx')
Sheet8 = Book1_2.parse(sheet_name = 'Sheet8')
print(Sheet8)
Sheet8.to_csv('Sheet8.csv',sep=',')
#Sheet 9
Sheet9 = pd.read_excel('Book1.xlsx', sheet_name = 'Sheet9', header = 0)
print(Sheet9)
Sheet9.to_csv('Sheet9.csv', sep=',')
#Sheet 10
Sheet10 = pd.read_excel('Book1.xlsx', sheet_name = 'Sheet10', header = 0)
print(Sheet10)
Sheet10.to_csv('Sheet10.csv', sep='-')