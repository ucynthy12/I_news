class Config:
   '''
   General configuration parent class
   '''
   NEWS_API_BASE_URL='https://newsapi.org/v2/{}?country=us&apiKey={}'
   NEWS_ARTICLE_URL='https://newsapi.org/v2/{}?apiKey={}'
  
 
class ProdConfig(Config):
   '''
   Production  configuration child class
 
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   pass
 
 
class DevConfig(Config):
   '''
   Development  configuration child class
 
   Args:
       Config: The parent configuration class with General configuration settings
   '''
 
   DEBUG = True