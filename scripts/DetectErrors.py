import language_tool_python
from newspaper import Article
from newspaper import fulltext
from newspaper import build
import traceback
import sys
from pandas import DataFrame
import pandas as pd
import numpy as np
import praw
import csv
tool = language_tool_python.LanguageTool('en-US')

data = pd.DataFrame(columns = ['URL', 'Typos', 'Total Words', 'Date', 'Upvotes', 'Upvote Ratio'])
df = pd.read_csv('data/news.csv')
# Take URL convert to text
file = open("articleinfo/redditArticles.txt", "r")
for i, url in enumerate(file.readlines()):
  try:
    article = Article(url.strip())
    article.download()
    article.parse()
    # sourceUrl = build(url)
    # print(sourceUrl.brand)
    #print(article.brand)
    matches = tool.check(article.text)
    if (len(article.text) == 0):
      print(url)
    else:
      if(article.publish_date == None):
        date = df.at[i, 'Reddit Date']
      else:
        date = str(article.publish_date)[0:10]
      upvotes = df.at[i, 'Upvotes']
      ratio = df.at[i, 'Upvote Ratio']
      path = "./fulltext/" + str(fileNum) + ".txt"
      fileNum += 1
      writeFile = open(path, "a+")
      writeFile.write(article.text)
      writeFile.close()
      data = data.append({'URL' : url, 'Typos' : len(matches), 'Total Words' : len(article.text), 'Date' : date, 'Upvotes': upvotes, 'Upvote Ratio': ratio}, ignore_index=True)
  except:
    print("Errored on: ", url)
    traceback.print_exception(*sys.exc_info())
file.close()
pd.DataFrame(data).to_csv("data/news.csv", index = False)
