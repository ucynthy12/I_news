
from flask import render_template
from app import app
from .request import get_article,get_source,search_article
from datetime import date
from flask import render_template,request,redirect,url_for

 
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
  

    today = date.today()
    i_news = get_source()
    # print(i_news)
   
    top_headlines = get_article('top-headlines')
    title = 'I_news - Your update on the latest news'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name = search_article))
    else:
        return render_template('index.html',day = today , title = title, headlines= top_headlines,news= i_news)

@app.route('/search/<article_name>')
def search(article_name):
    '''
    View functiomm to display the search results
    '''

    article_name_list = article_name.split(' ')
    article_name_format = '+'.join(article_name_list)
    searched_article = search_article(article_name_format)

    title = f'search results for {article_name}'
    return render_template('search.html', articles = searched_article)
  