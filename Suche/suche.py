from pymongo import MongoClient

connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)

# 1
dblist = client.list_database_names()
print('\n1:')
print('Databases')
for db in dblist:
    print('-', db)
print('Select Database:')
dbName = 'Restaurants'
db = client[dbName].list_collection_names()
print('Collections')
for collection in db:
	print('-' + collection)
collection = client[dbName]['restaurants']
res_list = []
for document in collection.find():
	if document['address']['street'] not in res_list: 
		res_list.append(document['address']['street']) 
		print(document)