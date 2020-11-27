
import urllib.request,json
from .models import Article,Sources

# Getting api key
api_key = None
# Getting the news base url
base_url = None
# Getting source url
news_url= None

def configure_request(app):
    global api_key,base_url,news_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']
    news_url=app.config['NEWS_SOURCE_LINK']
 
def get_source(category):

    '''
    Funcion that gets the json response to our url request
    '''
    get_source_url= news_url.format(category,api_key)

    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:

        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
 
        source_results= None
 
        if get_source_response['sources']:

            source_list = get_source_response['sources']
            source_results = process_source_results(source_list)
 
    return source_results
 
def process_source_results(source_list):

    '''
    Function that processes the source of the article and transform them to a list of Objects
  
    Args:
        source_list: A list of dictionaries that contain sources details
  
    Returns:
        source_results: A list of source objects
    '''
 
    source_results = []
  
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description= source_item.get('description')
        url= source_item.get('url')
        category = source_item.get('category')
       

        source_object= Sources(id,name,description,url,category)
        source_results.append(source_object)

  
    return source_results


def get_article(category):


    '''
    Funcion that gets the json response to our url request
    '''
    get_article_url= base_url.format(category,api_key)

 
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
 
        article_results= None
 
        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)
 
    return article_results
 
def process_results(article_list):

    '''
    Function that processes the article result and transform them to a list of Objects
  
    Args:
       article_list: A list of dictionaries that contain articles details
  
    Returns:
       article_results: A list of article objects
   '''
 
    article_results = []
  
    for article_item in article_list:

        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt= article_item.get('publishedAt')
        content  = article_item.get('content')
      
        if urlToImage:

            article_object= Article(author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results
 

def search_article(category):
    # search_article_results = []
    search_article_url = 'https://newsapi.org/v2/sources?category={}&apiKey={}'.format(category,api_key)
    print(search_article_url)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['sources']:
            search_article_list= search_article_response['sources']
            search_article_results = process_results(search_article_list)
    
    return search_article_results

