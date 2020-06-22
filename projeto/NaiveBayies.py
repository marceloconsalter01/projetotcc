import pandas as pd
from pymongo import MongoClient
import json, os, csv
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
import time

from projeto.models import UpdateMongoPrevisao

DEBUG = True


def nbml(dados):
    #Mongodb = MongoClient('localhost', 27123)
    #db = Mongodb.dbcredit
    #dados = db.cadastro.find_one({"cpf": cpf})
    #print(dados)
    dict_data = [[
        #                'nome',
        #                'cpf',
        #                'email',
        'checking_status',
        'duration',
        'credit_history',
        'purpose',
        'credit_amount',
        'savings_status',
        'employment',
        'installment_commitment',
        'personal_status',
        'other_parties',
        'residence_since',
        'property_magnitude',
        'age',
        'other_payment_plans',
        'housing',
        'existing_credits',
        'job',
        'num_dependents',
        'own_telephone',
        'foreign_worker'],
        [
            #                [dados['nome'],
            #                dados['cpf'],
            #                dados['email'],
            dados['checking_status'],
            dados['duration'],
            dados['credit_history'],
            dados['purpose'],
            dados['credit_amount'],
            dados['savings_status'],
            dados['employment'],
            dados['installment_commitment'],
            dados['personal_status'],
            dados['other_parties'],
            dados['residence_since'],
            dados['property_magnitude'],
            dados['age'],
            dados['other_payment_plans'],
            dados['housing'],
            dados['existing_credits'],
            dados['job'],
            dados['num_dependents'],
            dados['own_telephone'],
            dados['foreign_worker']]]

    myfile = open('teste_head.csv', 'w')
    with myfile:
        writer = csv.writer(myfile)
        writer.writerows(dict_data)

    base = pd.read_csv('creditfiltrado.csv', sep=';')
    print(base)
    base2 = pd.read_csv('teste_head.csv', sep=",")
    print(base2)
    base.class_result.unique()
    tempo_ini = time.time()
    X = base.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]].values
    y = base.iloc[:, 20].values
    z = base2.iloc[:, 0:20].values

    labelencoder = LabelEncoder()

    z[:, 0] = labelencoder.fit_transform(z[:, 0])
    z[:, 2] = labelencoder.fit_transform(z[:, 2])
    z[:, 3] = labelencoder.fit_transform(z[:, 3])
    z[:, 5] = labelencoder.fit_transform(z[:, 5])
    z[:, 6] = labelencoder.fit_transform(z[:, 6])
    z[:, 8] = labelencoder.fit_transform(z[:, 8])
    z[:, 9] = labelencoder.fit_transform(z[:, 9])
    z[:, 11] = labelencoder.fit_transform(z[:, 11])
    z[:, 13] = labelencoder.fit_transform(z[:, 13])
    z[:, 14] = labelencoder.fit_transform(z[:, 14])
    z[:, 16] = labelencoder.fit_transform(z[:, 16])
    z[:, 18] = labelencoder.fit_transform(z[:, 18])
    z[:, 19] = labelencoder.fit_transform(z[:, 19])

    X[:, 0] = labelencoder.fit_transform(X[:, 0])
    X[:, 2] = labelencoder.fit_transform(X[:, 2])
    X[:, 3] = labelencoder.fit_transform(X[:, 3])
    X[:, 5] = labelencoder.fit_transform(X[:, 5])
    X[:, 6] = labelencoder.fit_transform(X[:, 6])
    X[:, 8] = labelencoder.fit_transform(X[:, 8])
    X[:, 9] = labelencoder.fit_transform(X[:, 9])
    X[:, 11] = labelencoder.fit_transform(X[:, 11])
    X[:, 13] = labelencoder.fit_transform(X[:, 13])
    X[:, 14] = labelencoder.fit_transform(X[:, 14])
    X[:, 16] = labelencoder.fit_transform(X[:, 16])
    X[:, 18] = labelencoder.fit_transform(X[:, 18])
    X[:, 19] = labelencoder.fit_transform(X[:, 19])

    X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                      test_size=0.5,
                                                                      random_state=0)
    modelo = GaussianNB()
    modelo.fit(X_treinamento, y_treinamento)
    previsoes = modelo.predict(X_teste)
    previsoes2 = modelo.predict(z)
    print(previsoes2)
    accuracy_score(y_teste, previsoes)
    confusao = ConfusionMatrix(modelo, classes=['good', 'bad'])
    confusao.fit(X_treinamento, y_treinamento)
    confusao.score(X_teste, y_teste)

    UpdateMongoPrevisao(dados['cpf'],str(previsoes2))
    return previsoes2
