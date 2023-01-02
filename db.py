from pymongo import MongoClient
from config import mongo_host, mongo_port, mongo_user, mongo_user_pwd


class MongoDatabase:
    url = f'mongodb://{mongo_user}:{mongo_user_pwd}@{mongo_host}:{mongo_port}/vk_parser'
    client = MongoClient(url)
    db = client['vk_parser']
    users = db['users']

dbs = MongoDatabase()
