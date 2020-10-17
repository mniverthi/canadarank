import language_tool_python
from newspaper import Article
from newspaper import fulltext
import traceback
import sys
from pandas import DataFrame
import pandas as pd
import numpy as np
import praw

tool = language_tool_python.LanguageTool('en-US')

data = pd.DataFrame(columns = ['URL', 'Typos', 'Total Words', 'Date'])
redditDate = pd.read_csv('/newsranking/scripts/redditDate.csv')
# Take URL convert to text
file = open("../scripts/redditArticles.txt", "r")
for url in file.readlines():  
  try:
    article = Article(url.strip())
    article.download()
    article.parse()
    matches = tool.check(article.text)
    if (len(article.text) == 0):  
      print(url)
    else:
      if(article.publish_date == None):
        date = df.loc[df['URL'] == url]['Date']
        print(date)
      else:
        date = str(article.publish_date)[0:10]
      data = data.append({'URL' : url, 'Typos' : len(matches), 'Total Words' : len(article.text), 'Date' : date}, ignore_index=True)
  except:
    print("Errored on: ", url)
    traceback.print_exception(*sys.exc_info()) 
file.close()
print(data)
pd.DataFrame(data).to_csv("news.csv", index = False)


    