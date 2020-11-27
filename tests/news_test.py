import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Tom McCarthy","Republican officials finally forced into action on Covid-19 as reality bites - The Guardian", "Some GOP governors who for months toed Trump’s line on coronavirus, are performing U-turns on mask-wearing","https://www.theguardian.com/world/2020/nov/20/republicans-coronavirus-covid-19-governors-mask-mandates","https://i.guim.co.uk/img/media/d30fbba6eea55ae5aa4ef485fbb6dd7b3bf0f7d2/0_100_3000_1800/master/3000.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=3e757921ed1233fd508c213e13ff1ede","2020-11-20T13:52:00Z","After Republicans won big on election night in the state of Iowa, in Americas heartland, Governor Kim Reynolds claimed vindication for her light-handed approach to the coronavirus pandemic.\r\nSign up … [+7567 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()