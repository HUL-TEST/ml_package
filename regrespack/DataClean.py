
import pandas as pd
import numpy as np
from sklearn.utils import check_X_y

class clean:
    
    def __init__(self,X,y = None,target_col = None ,check_x_y = True,check_obj_cols = True):
        
        assert isinstance(y,pd.core.api.Series) | isinstance(y,np.core.ndarray), print('Target should be an array ')
        assert isinstance(X,pd.core.api.DataFrame) | isinstance(X,np.core.ndarray) , print('X must be a dataframe or numpy nd array')
        
        self.check_x_y = check_x_y
        self.check_obj_cols = check_obj_cols
        if target_col is None:
            self.X,self.y = X,y
        else:
           assert isinstance(target_col,str),print('Target column name must be string!')
           self.X,self.y = X.drop(target_col,axis = 1) ,X[target_col]
         
        self.data_clean()
        

    def treat_nans(self):
            
            if not isinstance(self.X,pd.core.api.DataFrame):
                self.X = pd.DataFrame(self.X)
            
            non_obj_cols = list(set(self.X.columns).difference(set(self.obj_cols)))
            self.X.fillna(self.X[non_obj_cols].mean(),inplace = True)
            
            def mode(self,s):
                self.X.loc[:,s].fillna(self.X.loc[:,s].value_counts().argmax(),inplace = True)
            
            if self.obj_cols!=None:
                for s in self.obj_cols:
                    self.mode(s)
                    
            
    def check_x_y_arr(self):
            ###check for consistency of X and y.
            self.ismissing = False
            try:
                self.X,self.y = check_X_y(self.X,self.y,y_numeric = True)
            except ValueError:
                self.ismissing = True
                return
        
    def get_obj_cols(self):
        ### This is to get list of columns that have object datatype:
            self.obj_cols = []
            if not isinstance(self.X,pd.core.api.DataFrame):
                self.X = pd.DataFrame(self.X)
        
            if self.X.select_dtypes(include = ['object']).columns.tolist()!= None:
                self.obj_cols = self.X.select_dtypes(include = ['object']).columns.tolist()
                
    
    def ohe_obj_cols(self):
        self.no_dummy_cols = []
        for s in self.obj_cols:
            if (self.X[s].nunique() <= 2) and (self.X[s].dtype != 'object'):
                self.no_dummy_cols.append(s)
                continue
        
        self.X = pd.get_dummies(data = self.X,columns = set(self.obj_cols).difference(set(self.no_dummy_cols)))
        
            
    def data_clean(self):
        
        if self.check_obj_cols:
            self.get_obj_cols()
        
        if self.check_x_y :
            self.check_x_y_arr()
            if self.ismissing != False:
                self.treat_nans()
        
        if self.obj_cols != [] : self.ohe_obj_cols()
        print('Completed cleaning')
        
    
    def return_clean_data(self):
        return self.X
