# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:31:37 2019

@author: Admin
"""

import numpy as np
import pandas as pd
## api for data cleaning
from sklearn.preprocessing import Imputer

imputer = Imputer(strategy="median" )


#Local Timestamp; Stats; Last; Bid; Ask; Exchange Timestamp; Exchange Name; Stats;
#ts_columns = ["Local_Timestamp", "Stats" , "Last" , "Bid" , "Ask" , "Exchange_Timestamp" , "Exchange_Name" , "Stats"] 
ts_data = pd.read_csv( "datastream_ETH-EUR.csv" )





