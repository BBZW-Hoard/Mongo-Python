from modules.MongoDb import MongoDb

db = MongoDb("mongodb://localhost:27017/")
db.getDatabase()
dbName = db.setDatabase()
db.getCollection(dbName)
collection = db.setCollection(dbName)
db.getDocuments(collection)
db.getIds(collection)