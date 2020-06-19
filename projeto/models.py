from pymongo import MongoClient
import pprint

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

for line in teste.find():
    pprint.pprint(line)
    print(line)
    objeto = str(line).split(',')
    print(objeto)

print(objeto[2])






