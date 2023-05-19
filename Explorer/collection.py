from pymongo import MongoClient
import bson

connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)

dblist = client.list_database_names()

# 1.
def getDatabase():
	print('\n1:')
	print('Databases')
	for db in dblist:
		print('-', db)
	print('Select Database:')
	validInput = True
	dbName = ''
	while validInput:
		dbName = input()
		if dbName not in dblist:
			print("No Database.")
			continue
		validInput = False
	getCollection(dbName)
		  
# 2.
print('\n2:')

def getCollection(dbName):
	db = client[dbName].list_collection_names()
	print('Collections')
	for collection in db:
		print('-' + collection)
	print('Select Collections:')
	getDocuments(dbName)

# 3
def getDocuments(dbName):
	print('\n3:')
	collectionName = input() #'customers'
	collection = client[dbName][collectionName]
	if collectionName not in client[dbName].list_collection_names():
		RestartProgram()
	print('Db: ' + dbName)
	print('Collection: ' + collectionName)
	print('Documents')
	for document in collection.find():
		print(document['_id'])
	print('Select Document:')
	getIds(dbName, collectionName)

# 4
def getIds(dbName,collectionName):
	print('\n4:')
	collection = client[dbName][collectionName]
	print('Db: ' + dbName)
	print('Collection: ' + collectionName)
	print('Document:')
	queryId = input()
	query = { "_id": bson.ObjectId(queryId) }
	document = collection.find_one(query)
	if document is None:
		RestartProgram()
	for k, v in document.items():
		print(k,':', v)
	print('Press any button to return:')
	input()
	getDatabase()

def RestartProgram():
	print('Press any button to return:')
	input()
	getDatabase()

getDatabase()