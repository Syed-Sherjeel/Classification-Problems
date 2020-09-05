# Titanic-Survival-Prediction-using-Decision-Tree
Purpose of this project is to model a statistical relationship between various various and chance of surviving.In this project we will apply decision tree to a.k.a entropy method to model relation between multiple explanatory variable and on dependent variable.Later we will try to improve the accuracy using hyperparameter tunning.
# Getting Stated
In order to be able to run this project we will be needing following packages. 
- numpy
- sklearn
- pandas
- matplotlib
# Installing dependencies
```
pip install sklearn 
pip install numpy 
pip install pandas 
pip install matplotlib 
```
# Usage Example
```
First store contents of redwine in  list X 
Following are explanatory variables.
- Survived: Outcome of survival (0 = No; 1 = Yes)
- Pclass: Socio-economic class (1 = Upper class; 2 = Middle class; 3 = Lower class)
- Name: Name of passenger
- Sex: Sex of the passenger
- Age: Age of the passenger (Some entries contain NaN)
- SibSp: Number of siblings and spouses of the passenger aboard
- Parch: Number of parents and children of the passenger aboard
- Ticket: Ticket number of the passenger
- Fare: Fare paid by the passenger
- Cabin Cabin number of the passenger (Some entries contain NaN)
- Embarked: Port of embarkation of the passenger (C = Cherbourg; Q = Queenstown; S = Southampton)

model.predict(X)
```
This will output a classification variable 0 or 1.whereas,1 stands for survived and 0 stands for not survived.
# License
This project is licensed under creative common 1.0.
