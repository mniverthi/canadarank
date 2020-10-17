def individualTest(url):
    article = Article(url)
    article.download()
    article.parse()
    matches = tool.check(article.text)
    if (len(article.text) == 0):
      print(url)
    else:
      print("Typos: ", len(matches), "Total Words: ", len(article.text))
      print(article.publish_date)