import json
from pymongo.mongo_client import MongoClient


db_uri = "mongodb+srv://renukesvr:qwertyok@cluster0.rhwqd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_uri)


db_name = "fitness"
col_gym = "gym"

db = client[db_name]

gym = db[col_gym]



file = open("gyms1.json","r")

data1 = file.read()

data = json.loads(data1)


for i in data:
    rk = gym.insert_one(i)
    print(rk)