# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 04:41:12 2020

@author: Precious Onu
"""
#Decision Tree Algorithm of flower
import pandas as pd
data = pd.read_csv('Iris.csv', index_col =0 )
y=data.iloc[:,[-1]].values; x = data.iloc[:,:-1]
from sklearn.preprocessing import LabelEncoder
X = LabelEncoder()
y = X.fit_transform(y.ravel())

from sklearn.model_selection import train_test_split as tts
X_train, X_test, y_train, y_test = tts(x,y, test_size = 0.3)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)
X_pred =  classifier.predict(X_train)


#Predicting the Value of y
y_pred = classifier.predict(X_test)

#Displaying the result
print(y_pred)

#Testing the accuracy of the model
from sklearn.metrics import accuracy_score as acs, confusion_matrix as cm
y_pred_cm = cm(y_test,y_pred)
print(y_pred_cm)
#The accuracy score of the model
y_pred_acs = acs(y_test,y_pred)
print('The Model accuracy score is ', y_pred_acs)