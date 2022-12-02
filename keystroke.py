import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_validate, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import svm


def learn_svm(data, train, test, target):
  columns = data.columns[1:14]
  X_train = train[columns]
  y_train = train[target]  

  X_test = test[columns]
  y_test = test[target]

  svmm = svm.SVC(kernel="linear")
  svmm.fit(X_train,y_train)

  res = svmm.predict(X_test)

  acuracia = metrics.accuracy_score(y_test,res)
  f1 = metrics.f1_score(y_test,res, average='weighted')
  print("SVM")
  print("Target: " + target)
  print("Acurácia: " + str(acuracia))
  print("F1 score: " + str(f1))

def learn_random_forest(data ,train, test, target):
  columns = data.columns[1:14]
  X_train = train[columns]
  y_train = train[target]  

  X_test = test[columns]
  y_test = test[target]

  random_forest = RandomForestClassifier(n_estimators=100, random_state = 42)
  random_forest.fit(X_train, y_train)


  res = random_forest.predict(X_test)

  acuracia = metrics.accuracy_score(y_test,res)
  f1 = metrics.f1_score(y_test,res, average='weighted')
  print("Random forest")
  print("Target: " + target)
  print("Acurácia: " + str(acuracia))
  print("F1 score: " + str(f1))

def learn_knn(data ,train, test, target):
  columns = data.columns[1:14]
  X_train = train[columns]
  y_train = train[target]  
  # print(y_train)

  X_test = test[columns]
  y_test = test[target]

  knn = KNeighborsClassifier(n_neighbors=1, metric = 'euclidean')
  knn.fit(X_train, y_train)

  res = knn.predict(X_test)
  # print(res)
  acuracia = metrics.accuracy_score(y_test,res)
  f1 = metrics.f1_score(y_test,res, average='weighted')
  # classificacao = metrics.classification_report(y_test,res)
  print("KNN")
  print("Target: " + target)
  print("Acurácia: " + str(acuracia))
  print("F1 score: " + str(f1))

  # cm = metrics.confusion_matrix(y_test,res)
  # print(cm)

def holdOut(data,targets):
  train, test = train_test_split(data, shuffle = True, test_size=0.2)
  for target in targets:
    learn_knn(data, train, test, target)
    learn_random_forest(data, train, test, target)
    learn_svm(data, train, test, target)  

def crossValidation(data, targets):
  columns = data.columns[1:14]
  X = data[columns]
  folds = StratifiedKFold(10)
  classifiers = [KNeighborsClassifier(n_neighbors=7, metric='euclidean'), svm.SVC(kernel="linear"), RandomForestClassifier(n_estimators=100, random_state = 42)]

  acurracies = []
  for i in range(len(targets)):
    acurracies.append([])
    # acurracys[i].append(targets[i])

  for i in range(len(targets)):
    y = data[targets[i]]
    for j in range(len(classifiers)):
      acurracy = []
      for train_index, test_index in folds.split(X, y):
            #print(train_index)
            #print(test_index)
            classifiers[j].fit(X.iloc[train_index],y.iloc[train_index])
            predicted = classifiers[j].predict(X.iloc[test_index])
            #print(sklearn.metrics.confusion_matrix(classes[test_index],predicted))
            acur = metrics.accuracy_score(y.iloc[test_index],predicted) 
            acurracy.append(acur)
            # print(acur)
      acurracies[i].append(acurracy)

  # print(len(acurracies[0]))
  # print(acurracies[0])
  for i in range(len(acurracies)):
    print("Classe:" + targets[i])
    for j in range(len(acurracies[i])):
      print(classifiers[j])
      mean = 0
      for k in range(len(acurracies[i][j])):
        print(str(k + 1) + ": " + str(acurracies[i][j][k]))
        mean += acurracies[i][j][k]
      # print("Média acurácia: {}".format(sum(acurracies[i][j])/len(acurracies[i][j])))
      mean = mean / len(acurracies[i][j])
      print("Média acurácia: " + str(mean))

def main():
  data = pd.read_csv("dataTarget.csv")
  targets = ["Target_Lilia", "Target_Wesley", "Target_Felipe", "Target_Madu", "Target_Jose", "Target_Roberto", "Target_Gerson"]  
  # holdOut(data,targets)
  crossValidation(data, targets)

if __name__ =="__main__":
  main()
