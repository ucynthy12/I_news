
from flask import render_template
from app import app
from .request import get_article,get_source
 
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    i_news = get_source()
    print(i_news)
   
    top_headlines = get_article('top-headlines')
    title = 'I_news - Your update on the latest news'
    return render_template('index.html',title = title, headlines= top_headlines,news= i_news)
 
  