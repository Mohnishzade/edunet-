Data Wrangling II Create an “Academic performance” dataset of students and perform the following operations using Python.

Scan all variables for missing values and inconsistencies. If there are missing values and/or inconsistencies, use any of the suitable techniques to deal with them.
Scan all numeric variables for outliers. If there are outliers, use any of the suitable techniques to deal with them.
Apply data transformations on at least one of the variables. The purpose of this transformation should be one of the following reasons: to change the scale for better understanding of the variable, to convert a non-linear relation into a linear one, or to decrease the skewness and convert the distribution into a normal distribution. Reason and document your approach properly.
import pandas as pd
import numpy as np

df=pd.read_csv('AcademicPerformanceNEW.csv')
df

df.head()

df.isnull().sum()

df.dropna()

reading_score_mean = df["reading score"].mean()
df["reading score"] = df["reading score"].fillna(reading_score_mean)

df

df.boxplot()

newdf = df[df["reading score"] > 20]
newdf

newdf.boxplot()
