import pandas as pd

excelfile = 'ALD_All.xlsx'

df = pd.read_excel(excelfile)

print(len(df.columns))

empty_cols = [col for col in df.columns if df[col].isnull().all()]
# Drop these columns from the dataframe
df.drop(empty_cols,
        axis=1,
        inplace=True)

print(len(df.columns))

grouped_df = df.groupby(['Loan Amount']).max()

print(grouped_df['Office/Branch'])