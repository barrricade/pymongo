from pymongo import MongoClient
import datetime
import bson
import json
import pprint
db = MongoClient().test
objects = db.objects
#uctnow和now的区别？
'''objects.insert_one({"last_modified":datetime.datetime.utcnow()})'''
'''objects.insert_one({"last modified":datetime.datetime.now()})'''
[pprint.pprint(doc) for doc in objects.find()]
#tz_aware
#db.tz_aware.insert_one({'date':datetime.datetime(2002,10,27,0,0)})
