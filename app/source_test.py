import unittest
from models import news

Sources = news.Sources

class SourceTest(unittest.TestCase):
        
    '''
    Test class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()