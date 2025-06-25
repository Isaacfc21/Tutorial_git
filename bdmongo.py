from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)

db_connection = client["aula01"]
print(db_connection)

collection = db_connection.get_collection("colecao01")
print(collection)

search_filter = {"Felipe": "Rafael"}

response = collection.find(search_filter)
for registro in collection.find(search_filter):
    print(registro)
    
collection.insert_one({
    "Rai": "Emerson",
    "Isaac": "Iron_Dev",
    "Guilherme": "Dev_Gohan"
})