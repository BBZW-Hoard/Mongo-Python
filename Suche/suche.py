from pymongo import MongoClient
from geopy.distance import geodesic
from bson.son import SON
import os


connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)

# 1
print("1")
dblist = client.list_database_names()
print('\n1:')
print('Databases')
for db in dblist:
    print('-', db)
print('Select Database:')
dbName = 'Restaurants'
db = client[dbName].list_collection_names()
print('Collections')
for collection in db:
	print('-' + collection)
collection = client[dbName]['restaurants']
res_list = []
for document in collection.find():
	if document['borough'] not in res_list: 
		res_list.append(document['borough']) 
		print(document['borough'])
# 2
print("2")
pipeline = [
        # Berechne den Durchschnitt des Ratings für jedes Restaurant
        {
            '$addFields': {
                'avgRating': { '$avg': '$grades.score' }
            }
        },
        # Sortiere absteigend nach dem Durchschnitts-Rating
        {
            '$sort': { 'avgRating': -1 }
        },
        # Begrenze das Ergebnis auf die top 3 Restaurants
        {
            '$limit': 3
        }
    ]
for document in collection.aggregate(pipeline):
	print(document)
le_perigord_coord = [-73.9749, 40.7625]

collection.create_index([("address.coord", "2dsphere")])
def find_nearest_restaurant():
    # 3
    print("3")
# Perform the geospatial query to find the nearest location
    nearest_location = collection.aggregate([
    {
        "$geoNear": {
            "near": {
                "type": "Point",
                "coordinates": le_perigord_coord
            },
            "distanceField": "distance",
            "spherical": True
        }
    },
    {
        "$limit": 1
    }
    ])

# Print the nearest location
    for location in nearest_location:
        print(location)

def find_nearest_restaurant_withSameCuisine():
	print("4")
	nearest_location = collection.aggregate([
    {
        "$geoNear": {
            "near": {
                "type": "Point",
                "coordinates": le_perigord_coord
            },
            "distanceField": "distance",
            "spherical": True,
	        "$filter": {
                "input": "$near",
               "as": "item",
               "cond": { "cuisine": "french" }
            }
        }
    },
    {
        "$limit": 1
    }
    ])
	for location in nearest_location: 
		print(location)
find_nearest_restaurant()
find_nearest_restaurant_withSameCuisine()
# Env
os.environ["MongoEnvString"] = "mongodb+srv://<User>:<Password>@cluster0.ndaadhc.mongodb.net/"
print(os.environ["MongoEnvString"])