import os
import json
import requests
postman_url = 'https://api.getpostman.com'


class Postman(object):
    def __init__(self, postman_api_key=os.getenv('postman_api_key')):
        self.headers = {
            'X-Api-Key': postman_api_key,
            'Content-Type': 'application/json'
        }
        self.payload = ''
        self.files = ''
        self.timeout = os.getenv('timeout') if os.getenv('timeout') not in ('', None) else 30
        self.redirects = os.getenv('redirects') if os.getenv('redirects') not in ('', None) else False
        self.postman_url = os.getenv('postman_url') if os.getenv('postman_url') not in ('', None) else postman_url
        self.collection_uid = os.getenv('collection_uid')
        self.environment_uid = os.getenv('environment_uid')
        self.monitor_uid = os.getenv('monitor_uid')

    def req(self, type, url, headers='', payload='', files='', redirects='', timeout=30):
        return requests.request(
            type,
            url,
            headers=headers if headers not in ('', {}, None) else self.headers,
            data=payload,
            files=files,
            allow_redirects=redirects if redirects not in ('', None) else self.redirects,
            timeout=timeout if timeout not in ('', None) else self.timeout
        )

    def get(self, url, headers='', uid=''):
        if uid not in ('', None):
            url = '{}/{}'.format(url, uid)
        return self.req('GET', url, headers=headers)

    def get_collection(self, collection_uid=''):
        url = '{}/collections'.format(self.postman_url)
        return self.get(url, collection_uid)

    def get_environment(self, environment_uid=''):
        url = '{}/environments'.format(self.postman_url)
        return self.get(url, environment_uid)

    def get_monitor(self, monitor_uid=''):
        url = '{}/monitors'.format(self.postman_url)
        return self.get(url, monitor_uid)

    def post(self, url, payload, headers=''):
        return self.req('POST', url, headers=headers, payload=payload)

    def post_collection(self, name, description=''):
        url = '{}/collections'.format(self.postman_url)
        payload = "{\n  \"collection\": {\n    \"variables\": [],\n    \"info\": {\n      \"name\": \"{}\",\n      \"description\": \"{}.\",\n      \"schema\": \"https://schema.getpostman.com/json/collection/v2.0.0/collection.json\"\n    },\n    \"item\": [\n      {\n        \"name\": \"This is a folder\",\n        \"description\": \"\",\n        \"item\": [\n          {\n            \"name\": \"Sample POST Request\",\n            \"request\": {\n              \"url\": \"echo.getpostman.com/post\",\n              \"method\": \"POST\",\n              \"header\": [\n                {\n                  \"key\": \"Content-Type\",\n                  \"value\": \"application/json\",\n                  \"description\": \"\"\n                }\n              ],\n              \"body\": {\n                \"mode\": \"raw\",\n                \"raw\": \"{\\n\\t\\\"data\\\": \\\"123\\\"\\n}\"\n              },\n              \"description\": \"This is a sample POST Request\"\n            },\n            \"response\": []\n          }\n        ]\n      },\n      {\n        \"name\": \"Sample GET Request\",\n        \"request\": {\n          \"url\": \"echo.getpostman.com/get\",\n          \"method\": \"GET\",\n          \"header\": [],\n          \"body\": {\n            \"mode\": \"formdata\",\n            \"formdata\": []\n          },\n          \"description\": \"This is a sample GET Request\"\n        },\n        \"response\": []\n      }\n    ]\n  }\n}".format(
            name, description)
        return self.req('POST', url, json.dumps(payload))


if __name__ == '__main__':
    postman = Postman()
    collections = postman.get_collection()
    print(collections.text)
