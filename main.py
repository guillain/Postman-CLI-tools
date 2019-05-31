import re
import os
import json
from dotenv import load_dotenv
from postman import Postman

load_dotenv()
postman = Postman()


def do_the_job(item):
    try:
        item_url = '{}/{}'.format(postman.postman_url, item)

        print(item, 'listing...')
        get_items = postman.get(item_url)

        print(item, 'dumping...')
        data = json.loads(get_items.text)
        for get_item in data[item]:
            if re.match(os.getenv('pattern_to_get'), get_item['name'], re.I):
                print('- ', get_item['id'], get_item['name'])
                with open('assets/Postman.' + item + '.' + get_item['name'] + '.json', "a") as item_dump_file:
                    item_dump_file.write(
                        postman.get('{}/{}'.format(item_url, get_item['id'])).text
                    )
    except:
        pass

do_the_job('workspaces')
do_the_job('collections')
do_the_job('environments')
