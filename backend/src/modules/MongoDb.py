from pymongo import MongoClient
import bson

class MongoDb():
	def __init__(self, connectionString, _id = None):
		if(_id is not None):
			self._id = _id
		connectionString = connectionString
		client = MongoClient(connectionString)
		self.client = client
		self.database = client["JukeBox"]
		self.collection = self.setCollection("songs")
		

	def findDocument(self, collection, document):
		return self.collection.find_one(
        {"_id": document.inserted_id}
    	)

	def InsertToDB(self, collection, document):
		return self.database[collection].insert_one(document)
	
	def UpdateDB(self, id, document):
		filter = {"_id": id}
		newvalues = {"$set": document}
		return self.collection.update_one(filter, newvalues)

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
		self.database = self.client[dbName]
		return
	
	def getCollection(self):
		collections = self.database.list_collection_names()
		print('Collections')
		for collection in collections:
			print('-' + collection)
		return collections

	def setCollection(self, collectionName):
		self.collection = self.database[collectionName]
		if collectionName not in self.database.list_collection_names():
			return None
		print('Db: ' + self.database.name)
		print('Collection: ' + collectionName)
		return self.collection

	def getDocuments(self, collection):
		print('Documents')
		for document in self.collection.find(limit=100):
			print(document['_id'])
		return list(self.collection.find(limit=100))
	
	def getDocumentFromId(self, collection):
		print('Select Document:')
		print('Document:')
		documentDict = []
		queryId = input()
		query = { "_id": bson.ObjectId(queryId) }
		document = self.collection.find_one(query)
		if document is None:
			self.RestartProgram()
			return
		for k, v in document.items():
			output = k,':', v
			documentDict.append(output)
			print(k,':', v)
		return documentDict

	def RestartProgram(self):
		print('Press any button to return:')
		input()
	
	def Close(self):
		self.client.close()