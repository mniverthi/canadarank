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

def computeScore(typoCount, totalWordCount, date, upvote, upvoteRatio, fakescore):
    typoRatio = typoCount / totalWordCount
    return 1
data = pd.DataFrame(columns = ['URL', 'Typos', 'Total Words', 'Date', 'Upvotes', 'Upvote Ratio'])
df = pd.read_csv('data/news.csv')
finalscore = []
for index, row in df.iterrows(): 
  finalscore.append(computeScore(df.at[i, 'Typos'],  df.at[i, 'Total Words'], df.at[i, 'Date'], df.at[i, 'Upvotes'],  df.at[i, 'Upvote Ratio'], df.at[i, 'Fake Score'])
  
df['Final Score'] = finalscore
pd.DataFrame(df).to_csv("data/news.csv", index = False)


