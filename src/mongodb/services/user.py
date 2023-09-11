from ..db import database

import logging
logger = logging.getLogger("__userService__")

def findOneUser(query):
    return database.users.find_one(query)

def findOneUserAndUpdate(query, update):
    return database.users.find_one_and_update(query, update)

def insertOneUser(userDoc):
    return database.users.insert_one(userDoc)

def updateOneUser(query, update):
    return database.users.update_one(query, update)