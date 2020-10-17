import language_tool_python
import requests
from newspaper import Article
from newspaper import fulltext
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Take URL convert to text
file = open("files.txt", "r")
for url in file.readlines():  
  
  article = Article(url, keep_article_html = True)
  article.download()
  article.parse()
  tool = language_tool_python.LanguageTool('en-US')
  matches = tool.check(article.text)
  print("Typos: %d Total Word: %d", len(matches), len(article.text))
  
file.close()