import pandas as pd
import numpy as np
import os

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

os.path.isfile('aug_train.csv')




def get_aug_train(url, cached=False):
    '''
    This function reads in url for aug_train data and writes data to
    a csv file if cached == False or if cached == True reads in aug_train_df from a csv file, returns df.
    '''
    aug_train_df = pd.read_csv(url)
    
    if cached == False or os.path.isfile('aug_train.csv') == False:
        
        # Read fresh data from db into a DataFrame.
        df = aug_train_df
        
        # Write DataFrame to a csv file.
        df.to_csv('aug_train.csv')
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('aug_train.csv', index_col=0)
        
    return df




