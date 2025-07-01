Data Wrangling Perform the following operations using Python on any open source dataset (e.g., data.csv)

1.Import all the required Python Libraries.

2.Locate an open source data from the web (e.g. https://www.kaggle.com). Provide a clear description of the data and its source (i.e., URL of the web site).

3.Load the Dataset into pandas data frame.

4.Data Preprocessing: check for missing values in the data using pandas insult(), describe() function to get some initial statistics. Provide variable descriptions. Types of variables etc. Check the dimensions of the data frame.

5.Data Formatting and Data Normalization: Summarize the types of variables by checking the data types (i.e., character, numeric, integer, factor, and logical) of the variables in the data set. If variables are not in the correct data type, apply proper type conversions.

6.Turn categorical variables into quantitative variables in Python. In addition to the codes and outputs, explain every operation that you do in the above steps and explain everything that you do to import/read/scrape the data set.


import pandas as pd
import numpy as np

df = pd.read_csv("AcademicPerformanceNEW.csv")

df.head()

df

df.isnull()

df.notnull()

df.isnull().sum()

df.notnull().sum()

df.describe()

df.size

print("shape :", df.shape)

df.ndim

df.info()

df=df.dropna()

df.dtypes

df['writing score'].astype(int)

df.loc[:, 'gender'] = df['gender'].replace({"Female": 0, "Male": 1})

df

df.head()
