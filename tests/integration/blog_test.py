from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):
    
    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test', 'Test Content')
        
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [{
                'title': 'Test Post',
                'content': 'Test Content'
            }]
        }

        self.assertDictEqual(b.json(), expected)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': []
        }      

        self.assertDictEqual(b.json(), expected) 