from re import S


class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,url,urlToImage,date,content):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.date = date
        self.content = content
        
        
