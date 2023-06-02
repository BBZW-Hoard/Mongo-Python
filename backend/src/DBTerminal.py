from modules.MongoDb import MongoDb
def RestartProgram():
	print('Press any button to return:')
	input()
	
db = MongoDb("mongodb://localhost:27017/")
print('\n1:')
print('Databases')
dblist = db.getDatabase()
for dbs in dblist:
	print('-', dbs)
print('Select Database:')
validInput = True
dbName = ''
while validInput:
	dbName = input()
	if dbName not in dblist:
		print("No Database.")
		continue
	validInput = False
db.setDatabase(dbName)
collections = db.getCollection()
print('Collections')
for collection in collections:
	print('-' + collection)
print('Select Collections:')
collectionName = input()
if collectionName not in collections:
	RestartProgram()
print('Db: ' + dbName)
print('Collection: ' + collectionName)
collection = db.setCollection(collectionName)
db.getDocuments()
print('Select Document:')
print('Document:')
queryId = input()
document = db.getDocumentFromId(queryId)
print(document)