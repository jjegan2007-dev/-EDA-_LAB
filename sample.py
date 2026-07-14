import pandas as pd

df = pd.read_csv('bodyPerformance.csv')
print('Dataset loaded successfully')
print(f'Total rows: {len(df)} | Total columns : {len(df.columns)}')

