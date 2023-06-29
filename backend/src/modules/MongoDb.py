from pymongo import MongoClient
import bson
import gridfs

class MongoDb():
	def __init__(self, connectionString, _id = None):
		if(_id is not None):
			self._id = _id
		connectionString = connectionString
		client = MongoClient(connectionString)
		self.client = client
		self.database = client["JukeBox"]
		self.songCollection = client["JukeBox"]["songs"]
		self.playlistCollection = client["JukeBox"]["playlists"]
		self.fsBucket = gridfs.GridFSBucket(client["JukeBox"])
		self.fs = gridfs.GridFS(client["JukeBox"])

	def findSongById(self, id):
		filter = {"_id": id}
		return self.songCollection.find_one(filter)
	
	def findPlaylistById(self, id):
		filter = {"_id": id}
		playlist = self.playlistCollection.find_one(filter)
		if playlist.get("songs") is None:
			return playlist
		songQuery = { "_id": { "$in": playlist["songs"]} }
		songs = list(self.songCollection.find(songQuery))
		playlist["songs"] = songs
		return playlist
	
	def findFileById(self, fileId):
		file = self.fsBucket.open_download_stream(fileId)
		return self.iterfile(file)
	
	def iterfile(self, file):
		with file as file_like:
			yield from file_like 	
	
	def findFileByName(self, fileName):
		file = self.fs.find_one({"filename": fileName})
		return self.iterfile(file)

	def InsertSong(self, document):
		return self.songCollection.insert_one(document)
	
	def InsertPlaylist(self, document):
		return self.playlistCollection.insert_one(document)
	
	def InsertFile(self, filename: str, file):
		fileId = self.fsBucket.upload_from_stream(filename, file)
		return fileId
	
	def UpdateSong(self, id, document):
		filter = {"_id": id}
		newvalues = {"$set": document}
		return self.songCollection.update_one(filter, newvalues)
	
	def UpdatePlaylist(self, id, document):
		filter = {"_id": id}
		newvalues = {"$set": document}
		return self.playlistCollection.update_one(filter, newvalues)
	
	def deleteSong(self, id):
		filter = {"_id": id}
		return self.songCollection.delete_one(filter)
	
	def deletePlaylist(self, id):
		filter = {"_id": id}
		return self.playlistCollection.delete_one(filter)

	def getSongs(self):
		return list(self.songCollection.find(limit=100))
	
	def getPlaylists(self):
		playlists = list(self.playlistCollection.find(limit=100))
		for playlist in playlists:
			if playlist.get("songs") is None:
				continue
			songQuery = { "_id": { "$in": playlist["songs"]} }
			songs = list(self.songCollection.find(songQuery))
			playlist["songs"] = songs
		return playlists
	
	def getSongsFromPlaylist(self, id):
		filter = {"_id": id}
		playlist = self.playlistCollection.find_one(filter)
		songQuery = { "_id": { "$in": playlist["songs"]} }
		songs = list(self.songCollection.find(songQuery))
		return songs
	
	def getDatabase(self):
		dblist = self.client.list_database_names()
		return dblist

	def setDatabase(self, dbName):
		self.database = self.client[dbName]
		return
	
	def setSongCollection(self, collectionName):
		self.songCollection = self.database[collectionName]
		return self.songCollection
	
	def setPlaylistCollection(self, collectionName):
		self.playlistCollection = self.database[collectionName]
		return self.songCollection
	
	def getCollection(self):
		return self.database.list_collection_names()
	
	def getSongDictFromId(self, id):
		documentDict = []
		query = { "_id": bson.ObjectId(id) }
		document = self.songCollection.find_one(query)
		if document is None:
			return None
		for k, v in document.items():
			output = k,':', v
			documentDict.append(output)
		return documentDict
	
	def Close(self):
		self.client.close()