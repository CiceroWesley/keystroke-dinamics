import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load


def learn_random_forest(data, target):
  columns = data.columns[1:14]
  X_train = data[columns]
  y_train = data[target]  
  print(X_train)
  print(y_train)
  random_forest = RandomForestClassifier(n_estimators=100, random_state = 42)
  random_forest.fit(X_train, y_train)
  dump(random_forest,target+".joblib")


def saveModels():
    data = pd.read_csv("dataTarget.csv")
    targets = ["Target_Lilia", "Target_Wesley", "Target_Felipe", "Target_Madu", "Target_Jose", "Target_Roberto", "Target_Gerson"]
    for target in targets:
        learn_random_forest(data, target)

def main():
  saveModels()


if __name__ =="__main__":
  main()