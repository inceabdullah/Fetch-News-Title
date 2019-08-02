from newspaper import Article

# get_title_from_news.get_title_from_news(url)

def get_title_from_news(url):
    article = Article(url)
    article.download()
    article.parse()
    url_title = article.title
    
    return url_title
