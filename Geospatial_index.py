from pymongo import MongoClient,GEO2D
import pprint
from bson.son import SON
db = MongoClient().geo_example
#db.places.create_index([("loc",GEO2D)])
'''result = db.places.insert_many([{"loc": [2, 5]},
                                {"loc": [30, 5]},
                                {"loc": [1, 2]},
                                {"loc": [4, 4]}]) '''
#查询靠近的文档
'''for doc in db.places.find({"loc": {"$near": [3, 6]}}).limit(3):
    pprint.pprint(doc)'''
#[pprint.pprint(doc) for doc in db.places.find({"loc": {"$near": [3, 6]}}).limit(3)]
#查询最大距离内的文档
'''query = {"loc":SON([("$near",[3,6]),("$maxDistance",100)])}
for doc in db.places.find(query).limit(3):
    pprint.pprint(doc)'''
#查询矩形内的文档
query = {"loc":{"$within":{"$box":[[2,2],[5,6]]}}}
for doc in db.palces.find(query).sort('_id'):
    pprint.pprint(doc)
#查询圆形范围的文档
query = {"loc":{"$within":{"$center":[[0,0],6]}}}
for doc in db.places.find(query):
    pprint.pprint(doc)