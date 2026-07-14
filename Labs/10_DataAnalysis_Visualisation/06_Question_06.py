# Write a Pandas program to find and replace the missing values in a given DataFrame 
# which do not have any valuable information.

import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

# find missing values
print(df.isnull().sum())

# we have missing values in scores

# filling missing values

# df.fillna({'score' : 'python'}, inplace = True)
# it will fill missing values in score column with python

# or we can also replace NaN with desired number
df.replace({np.nan : 2}, inplace = True)

print(df)