import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):
        
    '''
    Test class to test the behaviour of the Sources class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("aftenposten","Aftenposten","Norges ledende nettavis med alltid oppdaterte nyheter innenfor innenriks, utenriks, sport og kultur.", "https://www.aftenposten.no","general")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()