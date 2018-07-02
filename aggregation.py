#MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果。
import pymongo
from pymongo import MongoClient
from bson.son import SON
import pprint
db = MongoClient().aggregation_example
'''result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
                                {"x": 2, "tags": ["cat"]},
                                {"x": 2, "tags": ["mouse", "cat", "dog"]},
                                {"x": 3, "tags": []}])'''
pipeline = [
    {"$unwind": "$tags"},#对什么数据进行操作
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},#输出的格式，并且求和
    {"$sort": SON([("count", -1), ("_id", -1)])}]#输出的排序方式
pprint.pprint(list(db.things.aggregate(pipeline)))
