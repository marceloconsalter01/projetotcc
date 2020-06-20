import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
import time

Mongodb = MongoClient('localhost', 27123)

db = Mongodb.dbcredit


base = pd.read_csv('C:\\Users\\PICHAU\\Google Drive\\ML Script\\dados\\credit-g_filtrado.csv',sep=';')
base3 = pd.read_csv('C:\\Users\\PICHAU\\Google Drive\\ML Script\\dados\\teste.csv')
base2 = db.cadastro.find_one()

print(base3)
'''
#base = base.drop(columns = ['Unnamed: 0'])
base.class_result.unique()
tempo_ini = time.time()
X = base.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]].values
y = base.iloc[:, 20].values
z = base2.iloc[:,0:20].values

labelencoder = LabelEncoder()

z[:,0] = labelencoder.fit_transform(z[:,0])
z[:,2] = labelencoder.fit_transform(z[:,2])
z[:,3] = labelencoder.fit_transform(z[:,3])
z[:,5] = labelencoder.fit_transform(z[:,5])
z[:,6] = labelencoder.fit_transform(z[:,6])
z[:,8] = labelencoder.fit_transform(z[:,8])
z[:,9] = labelencoder.fit_transform(z[:,9])
z[:,11] = labelencoder.fit_transform(z[:,11])
z[:,13] = labelencoder.fit_transform(z[:,13])
z[:,14] = labelencoder.fit_transform(z[:,14])
z[:,16] = labelencoder.fit_transform(z[:,16])
z[:,18] = labelencoder.fit_transform(z[:,18])
z[:,19] = labelencoder.fit_transform(z[:,19])

X[:,0] = labelencoder.fit_transform(X[:,0])
X[:,2] = labelencoder.fit_transform(X[:,2])
X[:,3] = labelencoder.fit_transform(X[:,3])
X[:,5] = labelencoder.fit_transform(X[:,5])
X[:,6] = labelencoder.fit_transform(X[:,6])
X[:,8] = labelencoder.fit_transform(X[:,8])
X[:,9] = labelencoder.fit_transform(X[:,9])
X[:,11] = labelencoder.fit_transform(X[:,11])
X[:,13] = labelencoder.fit_transform(X[:,13])
X[:,14] = labelencoder.fit_transform(X[:,14])
X[:,16] = labelencoder.fit_transform(X[:,16])
X[:,18] = labelencoder.fit_transform(X[:,18])
X[:,19] = labelencoder.fit_transform(X[:,19])

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                  test_size = 0.5,
                                                                  random_state = 0)
modelo = GaussianNB()
modelo.fit(X_treinamento, y_treinamento)

previsoes = modelo.predict(X_teste)
previsoes2 = modelo.predict(z)

print(z)
print(previsoes2)


accuracy_score(y_teste, previsoes)

confusao = ConfusionMatrix(modelo, classes=['good','bad'])
confusao.fit(X_treinamento, y_treinamento)
confusao.score(X_teste, y_teste)
#print(confusao.score(X_teste, y_teste))

tempo_fim = time.time()
duracao1 = (tempo_fim-tempo_ini)/60
duracao = round(duracao1,2)

#print(tempo_ini)
#print(tempo_fim)
#print(duracao1)
#print(confusao)

#confusao.poof()

'''