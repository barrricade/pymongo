#MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果。
#$project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
#$match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
#$limit：用来限制MongoDB聚合管道返回的文档数。
#$skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
#$unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
#$group：将集合中的文档分组，可用于统计结果。
#$sort：将输入文档排序后输出。
#$geoNear：输出接近某一地理位置的有序文档。
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
    {"$unwind": "$tags"},#将文档中的某一个数组类型字段拆分成多条
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},#统计结果输出的格式，并且求和
    {"$sort": SON([("count", -1), ("_id", -1)])}]#输出的排序方式
pprint.pprint(list(db.things.aggregate(pipeline)))
