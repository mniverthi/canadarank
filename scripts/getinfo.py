import praw
import pandas as pd
from datetime import datetime, timezone

# grab url and CSV   
reddit = praw.Reddit(client_id="YOUR_INFO_HERE",
                     client_secret="YOUR_INFO_HERE",
                     password="YOUR_INFO_HERE",
                     user_agent="YOUR_INFO_HERE",
                     username="NewsRankBot")
# file we will pipe to 
file = open("articleinfo/redditArticles.txt", "w")
data = pd.DataFrame(columns = ['URL', 'Reddit Date', 'Upvotes', 'Upvote Ratio'])
# loop through reddit submissions under 'new' for canada subreddit
for submission in reddit.subreddit('canada').new(limit=100):
    data = data.append({'URL' : submission.url, 'Reddit Date' : datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')[0:10], 
        'Upvotes': submission.score, 'Upvote Ratio': submission.upvote_ratio}, ignore_index=True)
    file.write(submission.url + '\n')
pd.DataFrame(data).to_csv("data/redditDate.csv", index = False)
file.close()
