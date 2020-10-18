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
import math
tool = language_tool_python.LanguageTool('en-US')

data = pd.DataFrame(columns = ['URL', 'Typos', 'Total Words', 'Date', 'Upvotes', 'Upvote Ratio','Fake Score', 'Bias'])
df = pd.read_csv('data/news1.csv') #Shouldnt this be news1?
finalscore = []
meanTypos, meanTotalWords, meanUpvote, meanUpvoteRatio, meanFakeScore = df['Typos'].mean(), df['Total Words'].mean(), df['Upvotes'].mean(), df['Upvote Ratio'].mean(), df['Fake Scores'].mean()

def computeScore(typoCount, totalWordCount, date, upvote, upvoteRatio, fakescore, bias):
  if bias == 10:
    return -10000000
  #bias = -4 when the source doesn't have an associated bias calculation
  if bias == -4:
    bias = 1
  if (typoCount == 0) :
    typoCount = 1
  typorating = (1 / (typoCount / totalWordCount)) / (1 / (meanTypos / meanTotalWords))
  if (upvote != 0 and meanUpvoteRatio != 0):
    upvoterating = (upvoteRatio * math.log(upvote)) / (meanUpvote * math.log(meanUpvoteRatio))
  else: 
    upvoterating = -.50
  biasscore = 2 - abs(bias)
  fakerating = meanFakeScore / fakescore
  return .5 * biasscore + 0.4 * typorating + 0.4 * fakerating + 0.2 * upvoterating

for i, row in df.iterrows(): 
  finalscore.append(computeScore(df.at[i, 'Typos'],  df.at[i, 'Total Words'], df.at[i, 'Date'], 
    df.at[i, 'Upvotes'],  df.at[i, 'Upvote Ratio'], df.at[i, 'Fake Scores'], df.at[i, 'Bias']))
  
df["Final Score"] = finalscore
df = df.sort_values("Final Score", ascending = False)
pd.DataFrame(df).to_csv("data/news.csv", index = False)


