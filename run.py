#Install the following before proceeding
#pip install pandas, wheel, openpyxl

import pandas as pd

# Read the first XLSX file with Pandas
df1 = pd.read_excel('first_file.xlsx')
rename_dict = {row.TAG: row.SHORT for row in df1.itertuples()}

# Read the second XLSX file in Python with pandas
df2 = pd.read_excel('sec_file.xlsx')

# Get a list with all matched TAG values in header names
matched = [tag for tag in df1.loc[:, 'TAG'] if tag in df2.columns]

# Replace the header names from TAG with SHORT and overwrite the second file
df2.rename(columns=rename_dict, inplace=True)
df2.to_excel('sec_file.xlsx')