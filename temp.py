# write a code for reading an excel file skipping 5 rows and then apply a melt function to convert to long format
# and then save the file as csv
import pandas as pd
import numpy as np
import os
import glob

# read the excel file
df = pd.read_excel('data.xlsx', skiprows=5)
# print(df.head())

# melt the dataframe
df_melt = df.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                  var_name='Year', value_name='Value')
