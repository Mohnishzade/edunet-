Data Analytics I Create a Linear Regression Model using Python/R to predict home prices using Boston Housing Dataset (https://www.kaggle.com/c/boston-housing). 
The Boston Housing dataset contains information about various houses in Boston through different parameters. There are 506 samples and 14 feature variables in this dataset. 
The objective is to predict the value of prices of the house using the given features.
import pandas as pd
 from sklearn.linear_model import LinearRegression
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import mean_squared_error, r2_score

 df = pd.read_csv("Boston.csv")

 df.head()

 df.columns

 X=df[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
       'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv']]
 y=df["medv"]

 X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
 )

 model = LinearRegression()
 model.fit(X_train, y_train)

 y_pred = model.predict(X_test)

 y_pred

 score = model.score(X_train, y_train)
 print("Training R² Score:", score)

 score = model.score(X_test, y_test)
 print("Training R² Score:", score)

 mse = mean_squared_error(y_test, y_pred)
 print("Mean Squared Error:", mse)


