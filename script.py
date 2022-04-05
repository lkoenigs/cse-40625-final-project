import pandas as pd

raw_data = pd.read_csv('pppub21.csv')
data = raw_data[['A_MARITL','A_SEX','A_HGA','A_AGE','PEAFEVER','WSAL_VAL']]
data.to_csv('data.csv', index=False)
