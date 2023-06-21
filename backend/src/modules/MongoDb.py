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
		

	def findDocument(self, document):
		return self.collection.find_one(
        {"_id": document.inserted_id}
    	)
	
	def findSongById(self, id):
		filter = {"_id": id}
		return self.collection.find_one(filter)

	def InsertToDB(self, document):
		return self.collection.insert_one(document)
	
	def UpdateDB(self, id, document):
		filter = {"_id": id}
		newvalues = {"$set": document}
		return self.collection.update_one(filter, newvalues)

	def getDatabase(self):
		dblist = self.client.list_database_names()
		return dblist

	def setDatabase(self, dbName):
		self.database = self.client[dbName]
		return
	
	def getCollection(self):
		return self.database.list_collection_names()

	def setCollection(self, collectionName):
		self.collection = self.database[collectionName]
		return self.collection

	def getDocuments(self):
		print('Documents')
		for document in self.collection.find(limit=100):
			print(document['_id'])
		return list(self.collection.find(limit=100))
	
	def getDocumentFromId(self, id):
		documentDict = []
		query = { "_id": bson.ObjectId(id) }
		document = self.collection.find_one(query)
		if document is None:
			return None
		for k, v in document.items():
			output = k,':', v
			documentDict.append(output)
		return documentDict
	
	def Close(self):
		self.client.close()