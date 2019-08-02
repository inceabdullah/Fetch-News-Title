from newspaper import Article

# 

def get_title_from_news(url)
    article = Article(url)
    article.download()
    article.parse()
    url_title = article.title
    
    return url_title
