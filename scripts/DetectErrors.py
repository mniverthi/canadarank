import language_tool_python
from newspaper import Article
from newspaper import fulltext
import traceback
import sys
from pandas import DataFrame
import pandas as pd
import numpy as np
import praw
import csv
tool = language_tool_python.LanguageTool('en-US')

data = pd.DataFrame(columns = ['URL', 'Typos', 'Total Words', 'Date'])
df = pd.read_csv('articleinfo/redditDate.csv')
# Take URL convert to text
file = open("articleinfo/redditArticles.txt", "r")
for i, url in enumerate(file.readlines()):  
  try:
    article = Article(url.strip())
    article.download()
    article.parse()
    matches = tool.check(article.text)
    if (len(article.text) == 0):  
      print(url)
    else:
      if(article.publish_date == None):
        date = df.at[i, 'Reddit Date']
      else:
        date = str(article.publish_date)[0:10]
      data = data.append({'URL' : url, 'Typos' : len(matches), 'Total Words' : len(article.text), 'Date' : date}, ignore_index=True)
  except:
    print("Errored on: ", url)
    traceback.print_exception(*sys.exc_info()) 
file.close()
pd.DataFrame(data).to_csv("data/news.csv", index = False)


    