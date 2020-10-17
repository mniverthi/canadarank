import praw
import pandas as pd
from datetime import datetime, timezone

#grab url and CSV
    
reddit = praw.Reddit(client_id="VtubGoPRN3oLtg",
                     client_secret="XMgArUXTZz40OaWLKM046twdrJk",
                     password="ppF7egPkBAqT4V5",
                     user_agent="ranker by u/newrankbot",
                     username="NewsRankBot")
#file we will pipe to 
file = open("articleinfo/redditArticles.txt", "w")
data = pd.DataFrame(columns = ['URL', 'Reddit Date'])
#loop through reddit submissions under 'new' for canada subreddit
for submission in reddit.subreddit('canada').new(limit=100):
    data = data.append({'URL' : submission.url, 'Reddit Date' : datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')[0:10]}, ignore_index=True)
    file.write(submission.url + '\n')
pd.DataFrame(data).to_csv("data/redditDate.csv", index = False)
file.close()
