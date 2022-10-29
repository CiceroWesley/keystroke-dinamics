import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
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

def main():
  data = pd.read_csv("datatarget.csv")
  train, test = train_test_split(data, shuffle = True, test_size=0.333)
  learn_knn(data, train, test, "Target_Lilia")
  learn_knn(data, train, test, "Target_Wesley")
  learn_random_forest(data, train, test, "Target_Lilia")
  learn_random_forest(data, train, test, "Target_Wesley")
  learn_svm(data, train, test, "Target_Lilia")
  learn_svm(data, train, test, "Target_Wesley")

if __name__ =="__main__":
  main()

# # print(columns)
# #Lilia
# X_train = train[columns]
# y_train = train["Target_Lilia"]

# #Wesley
# y_train_2 = train["Target_Wesley"]
# y_test_2 = test["Target_Wesley"]

# # print(y_train_2)
# # print(y_test_2)
# # print(X_train)
# # print(y_train)
# X_test = test[columns]
# y_test = test["Target_Lilia"]
# # print(X_test)
# # print(y_test)
# n_neighbors = 5

# knn = KNeighborsClassifier(n_neighbors=n_neighbors, metric = 'euclidean')
# knn.fit(X_train, y_train)

# res = knn.predict(X_test)
# # print(res)

# acuracia = metrics.accuracy_score(y_test,res)
# classificacao = metrics.classification_report(y_test,res)
# # print(acuracia)
# print(classificacao)

# knn.fit(X_train, y_train_2)
# res2 =knn.predict(X_test)
# print(res2)
# acuracia = metrics.accuracy_score(y_test_2,res2)
# print(acuracia)

