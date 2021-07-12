#Imports 
import numpy as np
import pandas as pd
from scipy import stats
from math import sqrt
from datetime import datetime

#skelearn imports
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score


#Visualization
import matplotlib.pyplot as plt
import seaborn as sns



# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")





def data_split(df):
    '''
    This function take in the aug_train data acquired,
    performs a split and stratifies target column.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.target)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.target)
    return train, validate, test





def get_heatmap(col_list, target,  color = 'mako'):
    '''
    This method will return a heatmap of all variables and there relation to logerror
    '''
    plt.figure(figsize=(14,12))
    heatmap = sns.heatmap(col_list.corr()[[target]].sort_values(by=target, ascending=False), annot=True, linewidth=0.5,fmt = '.0%',cmap = color, center = 0)
    heatmap.set_title('Features  Correlating with {}'.format(target))
    
    return heatmap
