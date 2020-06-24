from pymongo import MongoClient
from datetime import date
import pprint

DEBUG = True
Mongodb = MongoClient('localhost', 27123)

db = Mongodb.dbcredit


def InsertMongo(data,selecao_nome, selecao_cpf, selecao_email, selecao_1, selecao_2, selecao_3, selecao_4,
                selecao_5, selecao_6, selecao_7, selecao_8, selecao_9, selecao_10,
                selecao_11, selecao_12, selecao_13, selecao_14, selecao_15, selecao_16,
                selecao_17, selecao_18, selecao_19, selecao_20):
    existing_document = db.cadastro.find_one({"cpf": selecao_cpf})

    if not existing_document:
        status = True
        db.cadastro.insert_many(
            [
                {   "data": data,
                    "nome": selecao_nome,
                    "cpf": selecao_cpf,
                    "email": selecao_email,
                    "checking_status": selecao_1,
                    "duration": selecao_2,
                    "credit_history": selecao_3,
                    "purpose": selecao_4,
                    "credit_amount": selecao_5,
                    "savings_status": selecao_6,
                    "employment": selecao_7,
                    "installment_commitment": selecao_8,
                    "personal_status": selecao_9,
                    "other_parties": selecao_10,
                    "residence_since": selecao_11,
                    "property_magnitude": selecao_12,
                    "age": selecao_13,
                    "other_payment_plans": selecao_14,
                    "housing": selecao_15,
                    "existing_credits": selecao_16,
                    "job": selecao_17,
                    "num_dependents": selecao_18,
                    "own_telephone": selecao_19,
                    "foreign_worker": selecao_20
                }
            ]
        )
    else:
        status = False
    return status


def FindMongoAll():
    return db.cadastro.find()


def FindMongoOne(value):
    return db.cadastro.find_one({"cpf": value})


def UpdateMongo(selecao_nome, selecao_cpf,data, selecao_email, selecao_1, selecao_2, selecao_3, selecao_4,
                selecao_5, selecao_6, selecao_7, selecao_8, selecao_9, selecao_10,
                selecao_11, selecao_12, selecao_13, selecao_14, selecao_15, selecao_16,
                selecao_17, selecao_18, selecao_19, selecao_20):
    query = {"cpf": selecao_cpf}
    newvalues = {"$set": {
        "nome": selecao_nome,
        "cpf": selecao_cpf,
        "data2": data,
        "email": selecao_email,
        "checking_status": selecao_1,
        "duration": selecao_2,
        "credit_history": selecao_3,
        "purpose": selecao_4,
        "credit_amount": selecao_5,
        "savings_status": selecao_6,
        "employment": selecao_7,
        "installment_commitment": selecao_8,
        "personal_status": selecao_9,
        "other_parties": selecao_10,
        "residence_since": selecao_11,
        "property_magnitude": selecao_12,
        "age": selecao_13,
        "other_payment_plans": selecao_14,
        "housing": selecao_15,
        "existing_credits": selecao_16,
        "job": selecao_17,
        "num_dependents": selecao_18,
        "own_telephone": selecao_19,
        "foreign_worker": selecao_20
    }}
    x = db.cadastro.update_one(query, newvalues)

    print(x.modified_count, "documents updated.")


def DeleteClient_One(cpf_value):
    print(cpf_value)
    return db.cadastro.delete_one({"cpf": cpf_value})


def UpdateMongoPrevisao(selecao_cpf, previsao):
    if previsao == "['good']":
        previsao = 'Bom Pagador'
    elif previsao == "['bad']":
        previsao = 'Mau Pagador'

    query = {"cpf": selecao_cpf}
    newvalues = {"$set": {
        "previsao_pag": previsao
    }}
    x = db.cadastro.update_one(query, newvalues)

    print(x.modified_count, "documents updated.")


def FindMongoStatus(value):
    return db.cadastro.find_one({"previsao_pag": value})

def getdata():
    data = date.today()
    data_atual = data.strftime('%d/%m/%Y')
    print(data_atual)
    return data_atual

