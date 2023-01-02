from config import vk_api_key
import json
import requests
from typing import NamedTuple, List
from exceptions import ErrorWithCode


class Vk_Response(NamedTuple):
    count: int
    items: List[dict]


v = 5.131


def group_users_request(group_id: int, offset: int) -> Vk_Response:
    url = 'https://api.vk.com/method/groups.getMembers'
    params = {
        'group_id': group_id,
        'sort': 'id_asc',
        'offset': offset,
        'count': 1000,
        'fields': [
            'bdate', 'can_post', 'can_see_all_posts',
            'can_see_audio', 'can_write_private_message', 'city' ,
            'common_count', 'connections', 'contacts' ,
            'country', 'domain', 'education' ,
            'has_mobile', 'last_seen', 'lists' ,
            'online', 'online_mobile', 'photo_100' ,
            'photo_200', 'photo_200_orig', 'photo_400_orig' ,
            'photo_50', 'photo_max', 'photo_max_orig' ,
            'relation', 'relatives', 'schools' ,
            'sex', 'site', 'status', 'universities'],
        'access_token': vk_api_key,
        'v': v
    }

    response = json.loads(
        requests.get(
            url, params=params
        ).text
    )

    if 'error' in response.keys():
        error_code = response['error']['error_code']
        ErrorWithCode(error_code)

    return Vk_Response(count=len(response['response']['items']),
                       items=response['response']['items'])

def user_friends_request(user_id):
    url = 'https://api.vk.com/method/friends.get'
    params = {
        'user_id': user_id,
        'sort': 'id_asc',
        'count': 1000,
        'fields': [
            'bdate', 'can_post', 'can_see_all_posts',
            'can_see_audio', 'can_write_private_message', 'city' ,
            'common_count', 'connections', 'contacts' ,
            'country', 'domain', 'education' ,
            'has_mobile', 'last_seen', 'lists' ,
            'online', 'online_mobile', 'photo_100' ,
            'photo_200', 'photo_200_orig', 'photo_400_orig' ,
            'photo_50', 'photo_max', 'photo_max_orig' ,
            'relation', 'relatives', 'schools' ,
            'sex', 'site', 'status',
            'universities'],
        'access_token': vk_api_key,
        'v': 5.131
    }

    response = json.loads(
        requests.get(
            url, params=params
        ).text
    )

    if 'error' in response.keys():
        error_code = response['error']['error_code']
        ErrorWithCode(error_code)

    return Vk_Response(
            count=len(response['response']['items']),
            items=response['response']['items']
        )

def get_user_posts():
    posts = json.loads(
        requests.get('https://api.vk.com/method/wall.get', params={
            'owner_id': user_id,
            'count': 100,
            'access_token': vk_api_key,
            'v': 5.131
            }
        ).text
    )

def get_user_posts_likes():
    likes = json.loads(
        requests.get('https://api.vk.com/method/wall.getLikes', params={
            'owner_id': user_id,
            'post_id': post_id,
            'count': 1000,
            'access_token': vk_api_key,
            'v': 5.131
            }
        ).text
    )

