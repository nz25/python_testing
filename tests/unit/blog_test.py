from unittest import TestCase
from app.blog import Blog

class BlogTest(TestCase):
    
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test']
        self.assertEqual(b.__repr__(), 'Test by Test Author: 0 posts')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf: 1 posts')

