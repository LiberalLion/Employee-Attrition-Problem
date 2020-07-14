import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import scipy
import xlrd
import openpyxl

currentdata = pd.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx', sheet_name = 'Existing employees')
leftdata = pd.read_excel('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx', sheet_name = 'Employees who have left')
leftdata.rename(columns={'Employee': 'Emp ID'}, inplace=True)
leftdata.drop_duplicates(subset=['Emp ID'])

WA = leftdata[leftdata['Work_accident']>0]
WA1 = WA.groupby(['dept'])['Work_accident'].sum()
WA1.plot(kind='bar')
WA1
#%%
leftdatax= leftdata.copy()
currentdatax = currentdata.copy()
leftdatax['Status']= 1
currentdatax['Status']=0
Total_employees = pd.concat([leftdatax,currentdatax], axis = 0)
Total_employees.columns
X = Total_employees.iloc[:,-10:-1]
Y = Total_employees.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['dept'] = le.fit_transform(X['dept'])
X['salary'] = le.fit_transform(X['salary'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)

#RandomFscore = []
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 71, random_state=0)
classifier.fit(X_train,y_train)
X_pred = classifier.predict(X_train)
y_pred = classifier.predict(X_test)

#Testing the model accuracy (Training)
from sklearn.metrics import accuracy_score as acs
from sklearn.metrics import confusion_matrix as cm
score = acs(y_train,X_pred)
matrix = cm(y_train,X_pred)


#Testing the Model Validity
Tscore = acs(y_test,y_pred)
Tmatrix = cm(y_test,y_pred)
