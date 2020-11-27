from . import main
from ..request import get_article,get_source,search_article
from datetime import date
from flask import render_template,request,redirect,url_for

 
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
  

    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    # print(d2)
    business_news = get_source('business')
    entertainment_news = get_source('entertainment')
    general_news = get_source('general')
    health_news = get_source('health')
    science_news = get_source('science')
    sports_news = get_source('sports')

  
    top_headlines = get_article('top-headlines')
    title = 'I_news - Your update on the latest news'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name = search_article))
    else:
        return render_template('index.html',day = d2, title = title, headlines= top_headlines, business = business_news , entertainment = entertainment_news , general = general_news , health = health_news , science = science_news , sports = sports_news)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''

    article_name_list = article_name.split(' ')
    article_name_format = '+'.join(article_name_list)
    searched_article = search_article(article_name_format)

    title = f'search results for {article_name}'
    return render_template('search.html', articles = searched_article)
  