Descriptive Statistics - Measures of Central Tendency and variability Perform the following operations on any open source dataset (e.g., data.csv)

Provide summary statistics (mean, median, minimum, maximum, standard deviation) for a dataset (age, income etc.) with numeric variables grouped by one of the qualitative (categorical) variable. For example, if your categorical variable is age groups and quantitative variable is income, then provide summary statistics of income grouped by the age groups. Create a list that contains a numeric value for each response to the categorical variable.
Write a Python program to display some basic statistical details like percentile, mean, standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris- versicolor’ of iris.csv dataset. Provide the codes with outputs and explain everything that you do in this step.
import pandas as pd
import numpy as np

df=pd.read_csv('Employee_Salary_Dataset.csv')

data = {
    'Age_group': ['18-25', '18-25', '26-35', '26-35', '36-45', '36-45'],
    'Salary': [15000, 18000, 25000, 30000, 40000, 45000]
}

df=pd.DataFrame(data)

df.median(numeric_only=True)

grouped=df.groupby('Age_group')['Salary']

grouped.describe()

print("\nincomme list by group : \n ",grouped.apply(list))

import seaborn as sns

iris =sns.load_dataset("iris")
df=pd.read_csv('iris.csv')


for species in iris['species'].unique():
    print(f"\nStatistics for {species.upper()}:\n")
    print(iris[iris['species'] == species].describe(percentiles=[0.25, 0.5, 0.75]))


or

setosa = df['Species'] == 'Iris-setosa'
print(df[setosa].describe())
  

print('\nIris-versicolor')
setosa = df['Species'] == 'Iris-versicolor'
print(df[setosa].describe())

print('\nIris-virginica')
setosa = df['Species'] == 'Iris-virginica'
print(df[setosa].describe()
