import pandas as pd

data = pd.read_csv("RAW_credit_test.csv")
print("The actual Raw Data")
print(data)
print("\n")
print("the size o fthe data is = ",data.shape)
print("Total number of empty rows in the csv files are")
empty = data.isnull().sum()
print(empty)
data = data.dropna()
print("After remove of blank row empty rows")
print(data.shape)
data.to_csv("Filtered_cr.csv",index=False)
print("The filtered csv is created ")


