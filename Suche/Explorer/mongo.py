from pymongo import MongoClient

connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)

print(client.server_info()) 