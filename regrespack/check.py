help(regrespack)
import regrespack

from regrespack import *
from sklearn.datasets import load_boston
import statsmodels.api as sm
from regrespack import DataClean
import pandas as pd
import numpy as np

dc = DataClean

X , y = load_boston().data, load_boston().target

X_nan = pd.DataFrame(X.copy())
X_nan.loc[[0,16,50,150,210],[0,3,5,10]] = np.nan 
clean_X = dc.clean(X_nan,y).return_clean_data()
clean_X.isna().any()

clean_X.head()
clean_X.isna().any()

model = train_pred.mltest(clean_X,y)
model.train(model = sm, model_name = 'lr')
model.predict(X,y)




