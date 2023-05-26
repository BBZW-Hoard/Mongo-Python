from modules.MongoDb import MongoDb    
db = MongoDb("mongodb://localhost:27017/")
db.getDatabase()
db.setDatabase()
db.getCollection()
collection = db.setCollection()
db.getDocuments(collection)
db.getDocumentFromId(collection)