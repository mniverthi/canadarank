from newspaper import Article
from newspaper import fulltext
from newspaper import build
import traceback
import sys
from pandas import DataFrame
import pandas as pd
import csv

df = pd.read_csv('data/news.csv')
titles = []
# Take URL convert to text
for i, row in df.iterrows():
    url = df.at[i, 'URL']
    try:
        article = Article(url.strip())
        article.download()
        article.parse()
        title = article.title
        titles.append(title)
    except:
        print("Errored on: ", url)
        traceback.print_exception(*sys.exc_info())

# Title,Typos,Total Words,Date,Upvotes,Upvote Ratio,Fake Scores,Bias,Final Score

del df['URL']
df['Title'] = titles
cols = ['Title', 'Date', 'Final Score', 'Fake Scores', 'Bias', 'Typos', 'Total Words', 'Upvotes', 'Upvote Ratio']
df = df[cols]
df = df.sort_values('Final Score', ascending = False)
pd.DataFrame(df).to_csv("../app/data/news.csv", index = False)
