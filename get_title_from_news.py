from newspaper import Article

# get_title_from_news.get_title_from_news(url)

def get_title_from_news(url):
    article = Article(url)
    article.download()
    try:
        article.parse()
        url_title = article.title
    except:
        url_title = ""
        
    
    
    return url_title
