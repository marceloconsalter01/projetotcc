from pymongo import MongoClient
import pprint
DEBUG = True
Mongodb = MongoClient('localhost',27123)

db = Mongodb.dbcredit
'''
db.cadastro.insert_many(
    [
        {"nome": "Julio Gay viado",
        "cpf":  "000.999.88",
        "telefone":"43 9999-9977"}
    ]
)'''

teste = db.cadastro
##print(teste)



#for line in teste.find():
#   print(line['nome'])









