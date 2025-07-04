Data Visualization I

Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and contains information about the passengers who boarded the unfortunate Titanic ship. Use the Seaborn library to see if we can find any patterns in the data.
Write a code to check how the price of the ticket (column name: 'fare') for each passenger is distributed by plotting a histogram.
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = sb.load_dataset('titanic')
df.head()

df.info()

print("Missing Values: ")
print(df.isnull().sum())

df['age'].fillna(df['age'].median(), inplace=True)
df.isnull().sum()

fig, axes = plt.subplots(1,2, figsize=(8,4))
fig.suptitle('Histogram 1-Variables(Age & Fare)')
sb.histplot(data = df, x = 'age', ax = axes[0])
sb.histplot(data = df, x = 'fare', ax = axes[1])
plt.show()

fig, axes = plt.subplots(2,2, figsize = (16,9))
fig.suptitle('Histogram 2-Variables')
sb.histplot(data = df, x = 'age', hue = 'survived', multiple='dodge', ax = axes[0][0])
sb.histplot(data = df, x = 'fare', hue = 'survived', multiple='dodge', ax = axes[0][1])
sb.histplot(data = df, x = 'age', hue = 'sex', multiple='dodge', ax = axes[1][0])
sb.histplot(data = df, x = 'fare', hue = 'sex', multiple='dodge', ax = axes[1][1])
plt.show()
