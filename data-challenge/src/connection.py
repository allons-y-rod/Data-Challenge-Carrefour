from pymongo import MongoClient

client = MongoClient('mongodb://rod:rod@localhost:27017/')

db = client.rod_carrefour

trends_collection = db.trends
