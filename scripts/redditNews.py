import praw
reddit = praw.Reddit(client_id="VtubGoPRN3oLtg",
                     client_secret="XMgArUXTZz40OaWLKM046twdrJk",
                     password="ppF7egPkBAqT4V5",
                     user_agent="ranker by u/newrankbot",
                     username="NewsRankBot")
file = open("redditArticles.txt", "w")
for submission in reddit.subreddit('canada').new(limit=100):
    #file.write(submission.url + '\n')
    if ((name of csv)["date"] == 0) {
        submission.publish_date
    }
file.close()
    
