import os
import pandas as pd

merge_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
	if file.endswith('.csv'):
		merge_df = merge_df.append(pd.read_csv(file))

merge_df.to_csv('Merge Data.csv',index = False)