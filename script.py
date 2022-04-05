import pandas as pd

raw_data = pd.read_csv('pppub21.csv')
data = raw_data[['A_MARITL','A_SEX','A_HGA','A_AGE','PEAFEVER','PEARNVAL']]
data.to_csv('data.csv')
