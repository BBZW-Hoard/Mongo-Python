from modules.MongoDb import MongoDb

db = MongoDb("mongodb://localhost:27017/")
dbName = db.getDatabase()
collectionName = db.getCollection(dbName)
db.getDocuments(dbName, collectionName)