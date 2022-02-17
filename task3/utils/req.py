import ast
import logging
import requests

import json

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


class Request:
    def __init__(self):
        self.headers = {'accept': 'application/json',
                        'Content-Type': 'application/json',
                        'api_key': 'special_key'}
        self.base_url = 'https://petstore.swagger.io/v2'

    def post_request(self, endpoint, post_data):
        resp = requests.post(url=f'{self.base_url}/{endpoint}', headers=self.headers, json=post_data)
        c_str = resp.content.decode("UTF-8")
        res = {'code': resp.status_code, 'content': json.loads(c_str)}
        logging.info(f'POST response: {res}')
        return res

    def get_request(self, endpoint):
        resp = requests.get(url=f'{self.base_url}/{endpoint}', headers=self.headers)
        c_str = resp.content.decode("UTF-8")
        res = {'code': resp.status_code, 'content': json.loads(c_str)}
        logging.info(f'GET response: {res}')
        return res

    def put_request(self, endpoint, put_data):
        resp = requests.put(url=f'{self.base_url}/{endpoint}', headers=self.headers, data=put_data)
        c_str = resp.content.decode("UTF-8")
        content = ast.literal_eval(c_str)
        res = {'code': resp.status_code, 'content': content}
        logging.info(f'PUT response: {res}')
        return res

    def delete_request(self, endpoint):
        resp = requests.delete(url=f'{self.base_url}/{endpoint}', headers=self.headers)
        c_str = resp.content.decode("UTF-8")
        content = ast.literal_eval(c_str)
        res = {'code': resp.status_code, 'content': content}
        logging.info(f'PUT response: {res}')
        return res



