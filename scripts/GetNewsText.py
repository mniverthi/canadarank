from newspaper import Article
import traceback
import sys
import numpy as np
import praw




# Take URL convert to text
file = open("articleinfo/redditArticles.txt", "r")
for index, url in enumerate(file.readlines()):  
  try:
    article = Article(url.strip())
    article.download()
    article.parse()
    if (len(article.text) == 0):  
      print(url)
    else:
      path = "./text/"+str(index)+".txt"
      writeFile = open(path, "a+")
      writeFile.write(article.text)
      writeFile.close()
      
  except:
    print("Errored on: ", url)
    traceback.print_exception(*sys.exc_info()) 
file.close()



    