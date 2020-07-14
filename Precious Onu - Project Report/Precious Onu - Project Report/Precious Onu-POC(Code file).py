# -*- coding: utf-8 -*-
"""
Project problem statement and proposal"""
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import xlrd; import openpyxl
#%%
Excel = pd.ExcelFile('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx')
Emp_left = Excel.parse(sheet_name = 'Employees who have left', header =0)
Emp_exist = Excel.parse(sheet_name = 'Existing employees')
Emp_left = Emp_left.drop_duplicates(['Emp ID'])

#Exploratory Data Analysis
Emp_left.count()
Emp_left.count(axis='columns')
Emp_left.describe()
columns = Emp_left.columns
Emp_left.size
# sheet['dept'].unique()
Emp_left['dept'].value_counts()
#sheet['salary'].unique()
Emp_left['salary'].value_counts()    
Emp_left['promotion_last_5years'].value_counts()
#%%
#Plots of variables to understand data
''' plots to make would be histograms of variables, barchart, heatmaps and scatter,
for exploratory analysis of the data: keywords for using pandas plotting 
capabilities are scatter, hist, area, pie. seaborn to be used for heatmap ploting capabilities'''

#- Satisfaction level

x=Emp_left['satisfaction_level']
x.plot(kind = 'hist', bins=25, alpha = 0.8)
plt.title('Satisfaction level plot')
plt.xlabel('Satisfaction level')
plt.ylabel('Frequency')
plt.savefig('satisf.png', dpi = 600)

#- Last evaluation
xa = Emp_left['last_evaluation']
xa.plot.hist(bins=20, alpha = 0.8)
plt.title('Evaluation score distribution')
plt.xlabel('Last Evaluation Score')
plt.ylabel('Frequency')
plt.savefig('lasevl.png', dpi = 600)

#y = sb.jointplot(xa,x, kind = 'scatter').savefig('ploy.png', dpi =550)
#y.get_figure()

#- Average monthly hours distribution
Emp_left['average_montly_hours'].plot.hist(bins = 25,alpha=0.6)
plt.title('Average monthly hours distribution')
plt.xlabel('Average monthly hours')
plt.ylabel('Frequency')
plt.savefig('avgmonh.png', dpi = 600)

#- Number of project
Emp_left['number_project'].plot(kind = 'hist', bins = 10)
plt.title('Number of Projects distribution')
plt.xlabel('Number of Projects')
plt.ylabel('Frequency')
plt.savefig('numproj.png', dpi = 400)

#1 Evaluation score and Hours
Emp_left.plot(kind = 'scatter', x='last_evaluation',y ='average_montly_hours', )
plt.xlabel('Last Evaluation Score')
plt.ylabel('Average Monthly Hours')
plt.title('Evaluation score and Average Monthly Hours Plot')
plt.savefig('AvgnEval.png', dpi = 550)

#2 Evaluation score and Satisfaction
Emp_left.plot(kind = 'scatter', x='last_evaluation',y ='satisfaction_level', )
plt.xlabel('Last Evaluation Score')
plt.ylabel('Satisfaction level')
plt.title('Evaluation score and Satisfaction level Plot')
plt.savefig('EvalnSatisfaction.png', dpi = 550)

#Correlational Coefficient (Evaluation score and Satisfaction)
np.corrcoef(Emp_left.iloc[:,1],Emp_left.iloc[:,2])

#3
JP = sb.jointplot(Emp_left['last_evaluation'], Emp_left['satisfaction_level'])
JP.savefig('Evaluation n\' score joint plot.png')


#%%
# -Promotion_last_5years
promo = Emp_left.groupby(['promotion_last_5years'])['promotion_last_5years'].count()
promo.plot(kind='pie', autopct = '%1.1f%%', explode=[0,0.5], labels=['No','Yes'])
plt.title('Promoted within the past 5 years')
plt.ylabel('Percentage')
plt.savefig('promotion.png', dpi = 500)
# sheet['promotion_last_5years'].value_counts()

# -Time spend Company
time = Emp_left.groupby(['time_spend_company']).time_spend_company.count()
time.plot(kind='barh')
plt.savefig('time.png', dpi = 450)
Emp_left['time_spend_company'].value_counts()

# -Work accident
work_accident = Emp_left.groupby(['Work_accident']).Work_accident.count()
work_accident.plot(kind='pie', autopct = '%1.1f%%', explode=[0,0.5], labels=['No','Yes'])
Emp_left['Work_accident'].value_counts()

# - Salary level by Department
Depart = Emp_left.groupby(['dept', 'salary']).dept.count()
Depart.plot.bar()
plt.title('Barchart of Salary and Department')
plt.xlabel('Department and Salary')
plt.ylabel('Count')
plt.savefig('Salarylevelindept.png', dpi = 600)


# - Satisfaction level to department
deptsat = Emp_left.groupby(['dept'])['satisfaction_level'].median()
deptsat.plot(kind='bar')

# - Evaluation score to department
depteval = Emp_left.groupby(['dept'])['last_evaluation'].median()
depteval.plot(kind='bar')

# - Workaccident by Department
Work_accident = Emp_left[Emp_left['Work_accident']>0]
Work_accident = Work_accident.groupby('dept').Work_accident.sum()
Work_accident.plot(kind='barh')
plt.title('Accidents by Department')
plt.savefig('accidentbydept.png')

