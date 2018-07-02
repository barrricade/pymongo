import pymongo
from pymongo import MongoClient
db = MongoClient().test
help = db.help
help.insert_one({"name":"a"})