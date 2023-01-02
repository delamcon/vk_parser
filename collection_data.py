from enum import unique
import time
from reqs import Vk_Response, group_users_request
from exceptions import ExpiredApiKey


# добавляем id группы в данные пользователя
def add_groupId_to_user_data(user_data: dict, group_id: int) -> dict:
    if 'groups' not in user_data.keys():
        user_data['groups'] = []
    user_data['groups'].append(group_id)
    return user_data

# данная функция нужна чтобы превратить id пользователей в ключ "_id", для 
# дальнейшего сохранения в базе данных mongo, если нам придется обновлять 
# данные, то мы сможем их обновить по id пользователя довольно быстро
# (не придется искать сначала _id документа с id пользователя)
def _modify_users_id_key(users_response: Vk_Response):
    modify_users_list = []
    for user_data in users_response.items:
        user_data["_id"] = user_data.pop("id")
        modify_users_list.append(user_data)
    return Vk_Response(
                count=users_response.count,
                items=modify_users_list
            )       

def _request_with_error_handler(group_id, offset) -> Vk_Response:
    try:
        group_users_response: Vk_Response = group_users_request(group_id, offset)
        modify_group_users: Vk_Response = _modify_users_id_key(group_users_response)
    except ExpiredApiKey:
        print('Истек ключ апи')
        exit(1)
    return modify_group_users

def get_group_users(group_id: int) -> Vk_Response:
    group_users = []
    len_of_response = -1
    offset = 0
    
    while len_of_response != 0:
        several_group_users: Vk_Response = _request_with_error_handler(group_id, offset)
        offset += 1000
        len_of_response = len(several_group_users.items)
        group_users += several_group_users.items
        time.sleep(0.3)
        print(len(group_users))
    
    return Vk_Response(
                count=-1,
                items=group_users
            )

