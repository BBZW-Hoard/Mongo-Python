from modules.MongoDb import MongoDb    
db = MongoDb("mongodb://localhost:27017/")
db.getDatabase()
db.setDatabase()
db.getCollection()
print('Select Collections:')
collectionName = input()
collection = db.setCollection(collectionName)
db.getDocuments(collection)
db.getDocumentFromId(collection)