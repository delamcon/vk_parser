from db import MongoDatabase
from collection_data import get_group_users
from reqs import Vk_Response


mongo_db = MongoDatabase()
group_users: Vk_Response = get_group_users(-1)

mongo_db.users.insert_many(group_users.items)
print('users saved')

