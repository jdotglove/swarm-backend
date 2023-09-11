import pymongo

import certifi
from src.config import SWARM_MONGO_URI

ca = certifi.where()

# instantiate mongo client
client = pymongo.MongoClient(SWARM_MONGO_URI, tlsCAFile=ca)
database = client["mainStack"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)