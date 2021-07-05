import hashlib
import json
from typing import Dict

import httpx


class GravatarUser:
    BASE_URL = 'https://ru.gravatar.com/'

    def __init__(self, query: str):
        user_info = self.get_user_info(query)
        [setattr(self, name, value) for name, value in user_info.items()]

    @property
    def to_json(self):
        data = {'result': dict(self.__dict__.items())}
        return json.dumps(data, indent=2)

    @staticmethod
    def get_md5(query: str) -> str:
        return hashlib.md5(query.encode()).hexdigest()

    def get_query_str(self, query: str) -> str:
        url = self.BASE_URL + self.get_md5(query) + '.json'
        return url

    def get_user_info(self, query: str) -> Dict:
        url = self.get_query_str(query)
        response = httpx.get(url)
        if response.is_error:
            raise Exception(f'Error: Unable to get {url}. Status code: {response.status_code}')

        data, = response.json()['entry']

        user_info = {
            'id': data.get('id'),
            'email_hash': data.get('hash'),
            'url': data.get('profileUrl'),
            'alias': data.get('preferredUsername'),
            'thumb': data.get('thumbnailUrl'),
            'photos': data.get('photos'),
            'person': None if not data.get('name') else data.get('name').get('formatted'),
            'location': data.get('currentLocation'),
            'emails': data.get('emails'),
            'accounts': data.get('accounts'),
            'urls': data.get('urls')
        }

        return user_info


if __name__ == '__main__':
    # just input query email string and use 'to_json' property
    query_email = 'ras-nie@web.de'
    u = GravatarUser(query_email)
    result = u.to_json
    print(result)
