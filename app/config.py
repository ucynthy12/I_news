class Config:
   '''
   General configuration parent class
   '''
   NEWS_API_BASE_URL='https://newsapi.org/v2/{}?country=us&apiKey={}'
   # NEWS_SOURCE_LINK='https://newsapi.org/v2/sources?apiKey={}'
   NEWS_SOURCE_LINK='https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'

  
 
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
   NEWS_API_BASE_URL='https://newsapi.org/v2/{}?country=us&apiKey={}'
   # NEWS_SOURCE_LINK='https://newsapi.org/v2/sources?apiKey={}'
   NEWS_SOURCE_LINK='https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'



 
   DEBUG = True