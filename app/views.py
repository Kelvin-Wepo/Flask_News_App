from flask import Flask, render_template
from app import app
from app.request import get_news, get_sources




@app.route('/')
def index():
    news = get_news()
    '''
    View root page function that returns the index page and its data
    '''

   
    return render_template('index.html',articles=news )

@app.route('/sources')
def sources():
    '''
    View Function that returns the source page and its data
    '''
    
    sources = get_sources('sources')
    title = 'Home - Find the latest news highlights'
    return render_template('Sources.html', title=title, sources = sources)

     

