from pymongo import MongoClient
import bson

class MongoDb():
	def __init__(self, connectionString, _id = None):
		if(_id is not None):
			self._id = _id
		connectionString = connectionString
		self.client = MongoClient(connectionString)

	def getDatabase(self):
		dblist = self.client.list_database_names()
		print('\n1:')
		print('Databases')
		for db in dblist:
			print('-', db)
		return

	def setDatabase(self):
		dblist = self.client.list_database_names()
		print('Select Database:')
		validInput = True
		dbName = ''
		while validInput:
			dbName = input()
			if dbName not in dblist:
				print("No Database.")
				continue
			validInput = False
		return dbName
	
	def getCollection(self, dbName):
		db = self.client[dbName].list_collection_names()
		print('Collections')
		for collection in db:
			print('-' + collection)

	def setCollection(self, dbName):
		print('Select Collections:')
		collectionName = input()
		collection = self.client[dbName][collectionName]
		if collectionName not in self.client[dbName].list_collection_names():
			self.RestartProgram()
		print('Db: ' + dbName)
		print('Collection: ' + collectionName)
		return collection

	def getDocuments(self, collection):
		print('Documents')
		for document in collection.find():
			print(document['_id'])
	
	def getIds(self, collection):
		print('Select Document:')
		print('Document:')
		queryId = input()
		query = { "_id": bson.ObjectId(queryId) }
		document = collection.find_one(query)
		if document is None:
			self.RestartProgram()
		for k, v in document.items():
			print(k,':', v)
		print('Press any button to return:')
		input()

	def RestartProgram(self):
		print('Press any button to return:')
		input()
		self.getDatabase()