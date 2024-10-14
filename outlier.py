import pandas as pandas

df = pandas.read_csv('cleaned_train.csv')

#df = df.sort_values(by='Age')

#print(df.iloc[179]) #q1 = 20.5

#print(df.iloc[535]) #q3 = 38
# iqr = 38 - 20.5 = 17.5

#df = df.sort_values(by='Fare')

#print(df.iloc[179]) #q1 = 8.05

#print(df.iloc[535]) #q3 = 33.5
# iqr = 33.5 - 8.05 = 25.45

df = df.drop(df[(df['Age'] > 64)].index)
df = df.drop(df[(df['Fare'] > 72)].index)

df.to_csv('cleaned_train.csv', index=True)