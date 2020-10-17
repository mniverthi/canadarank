import praw
import pandas as pd
from datetime import datetime, timezone
    
reddit = praw.Reddit(client_id="VtubGoPRN3oLtg",
                     client_secret="XMgArUXTZz40OaWLKM046twdrJk",
                     password="ppF7egPkBAqT4V5",
                     user_agent="ranker by u/newrankbot",
                     username="NewsRankBot")
# file = open("redditArticles.txt", "w")
data = pd.DataFrame(columns = ['URL', 'Date'])
for submission in reddit.subreddit('canada').new(limit=100):
    data = data.append({'URL' : submission.url, 'Date' : datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')[0:10]}, ignore_index=True)
# file.close()
    
