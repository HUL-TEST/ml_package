# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_boston, load_diabetes
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm

X1, y1 = load_diabetes().data, load_diabetes().target
X2, y2= load_boston().data , load_boston().target


class mltest():
    
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        
    def train(self, model, model_name):
        if str(model_name) == 'lr':
            self.model_name = model_name
            X = self.X_train
            y = self.y_train
            self.fitted_model = model.OLS(y, X).fit()
            
        else:
            self.model_name = model_name
            self.fitted_model = model.fit(self.X_train, self.y_train)
        
    def predict(self, X_test, y_test):
        if self.model_name == 'lr':            
            y_pred = self.fitted_model.predict(X_test)
            print("Model Performance evaluation :")
            return self.fitted_model.summary()
        
        else:
            y_pred  = self.fitted_model.predict(X_test)
            print("Model Performance evaluation :\n")
            print("Mean Squared error of the {} is".format(self.model_name))
            return mean_squared_error(y_test, y_pred)
    