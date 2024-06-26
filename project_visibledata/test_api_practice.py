import unittest
import requests

class TestHnApi(unittest.TestCase):

    def test_status_codes(self):
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        r = requests.get(url)
        self.assertEqual(r.status_code,200)

    def get_list(self):
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        r = requests.get(url)
        if r.status_code == 200:
            return r
        else:
            return 0

    def test_each_item(self):
        r = self.get_list()
        if r == 0:
            return 0
        r_read = r.json()
        for item in r_read[:10]:
            ritem = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(item) + '.json')
            self.assertEqual(ritem.status_code,200)
        ritem = requests.get('https://hacker-news.firebaseio.com/v0/item' + '1234' + '.json')
        self.assertEqual(ritem.status_code,200)


unittest.main()