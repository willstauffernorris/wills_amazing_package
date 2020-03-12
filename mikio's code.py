import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import category_encoders as ce

def increase(x):
    return x+1

def decrease(x):
    return x-1

def multiply(x):
    return x*2

def divide(x):
    return x/1

def addtwo(x):
    return x+2

def addthree(x):
    return x+3

def name(x):
    return x + 10

def subtract(x):
    return x-3

def addfive(x):
    return x+5

class Preprocess:
  def __init__(self, df, target, feat):
    self.df = df
    self.target = target
    self.feat = feat
  
  def null(self):
    return self.df.isnull().sum()
  
  def split(self):

    training, testing = train_test_split(self.df.dropna())

    X_train = training[self.feat]
    y_train = training[self.target]

    X_test = testing[self.feat]
    y_test = testing[self.target]

    return X_train, y_train, X_test, y_test
  
  def encode(self, xtrain1, xtest1):
    encoder = ce.OrdinalEncoder()
    x_train_encode = encoder.fit_transform(xtrain1)
    x_test_encode = encoder.transform(xtest1)
    return x_train_encode, x_test_encode


class Modeling(Preprocess):
  # model parameter will be initialized by Modeling class
  def __init__(self, model, df, target, feat):
    # Preprocess will initialize these parameters
    super().__init__(df, target, feat)
    self.model = model

  def predict(self, xtrain, ytrain, xtest, ytest):
    self.model.fit(xtrain, ytrain)
    return self.model.score(xtest, ytest)