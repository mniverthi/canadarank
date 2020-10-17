import language_tool_python
from newspaper import Article
from newspaper import fulltext
import traceback
import sys

tool = language_tool_python.LanguageTool('en-US')



# Take URL convert to text
file = open("../scripts/articles.txt", "r")
i = 0
for url in file.readlines():  
  try:
    article = Article(url.strip())
    article.download()
    article.parse()
    matches = tool.check(article.text)
    if (len(article.text) == 0):
      print(url)
    else:
      print("Typos: ", len(matches), "Total Words: ", len(article.text))
  except:
    print("Errored on: ", url)
    traceback.print_exception(*sys.exc_info()) 

file.close()

    