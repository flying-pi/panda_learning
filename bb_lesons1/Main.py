import matplotlib.pyplot as plt
import pandas as pd  # this is how I usually import pandas
import sys  # only needed to determine Python version number
import matplotlib  # only needed to determine Matplotlib version number

# Enable inline plotting
# % matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print("__________________________________________________________________________________________________\n")

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names, births))

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
print(df)
print("__________________________________________________________________________________________________\n")

df.to_csv('births1880.csv',index=False,header=False)
locations = 'births1880.csv'
newDf = pd.read_csv(locations,header=None)
newDf1 = pd.read_csv(locations, names=['Names','Births'])
print(newDf)
print("__________________________________________________________________________________________________\n")
print(newDf1)
print("__________________________________________________________________________________________________\n")

Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted)
print("__________________________________________________________________________________________________\n")
print(df['Births'].max())
print("__________________________________________________________________________________________________\n")

# df['Births'].plot()

MaxName = df['Names'][df['Births'] == df['Births'].max()].values
print(MaxName)
print("__________________________________________________________________________________________________\n")