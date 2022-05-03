from app import app
import urllib.request,json
from .models  import news,sources    

News = news.News
Sources= sources.Sources


# Getting api key
api_key = '9fd82fc4cd6a48f3b9616c64a3f0ce4a'
base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
sources_base_url = 'https://newsapi.org/v2/top-headlines/{}?apiKey={}'

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

    ...
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        date = news_item.get('publishedAt')
        content = news_item.get('content')
        if urlToImage:
            news_object = News(author,title,description,url,urlToImage,date,content)    
            news_results.append(news_object)

    return news_results

def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_base_url.format(sources, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        # sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            # sources_results = process_sources(sources_results_list)
    return sources_results_list
def process_sources(sources_results_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    '''
    sources_list = []
    for source_item in sources_results_list:
            id = source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            url = source_item.get('url')
            category = source_item.get('category')
            language = source_item.get('language')
            country = source_item.get('country')

            if url:
                sources_object = Sources(id, category, language, country)
                sources_list.append(sources_object)
            
            return sources_list