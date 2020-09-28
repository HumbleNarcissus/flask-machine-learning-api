import json
from api.tests.base import BaseTestCase
from api.tests.utils import add_movie
class TestApi(BaseTestCase):
    # test api
    def test_get_movies(self):
        add_movie('Test', 'Test_url')
        add_movie('Test1', 'Test_url2')
        with self.client:
                response = self.client.get(
                    '/api/prediction',
                    content_type='application/json'
                )
                data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(data['movies']), 2)
    
    def test_post_movies(self):
        with self.client:
            response = self.client.post(
                '/api/prediction',
                data=json.dumps({
                    'title': 'test_title',
                    'url': 'test_url',
                    'comments': ['test1', 'test2']
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("test_title", data['result']['title'])
            self.assertIn("test_url", data['result']['url'])
            self.assertEqual(len(data['result']['comments']), 2)