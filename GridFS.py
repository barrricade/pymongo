from pymongo import MongoClient
import gridfs
import pprint
db=MongoClient().gridfs_example
fs = gridfs.GridFS(db)
a = fs.put(b"hello world")