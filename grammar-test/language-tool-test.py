import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
import urllib as urllib

# Take URL convert to text
NEWS_ARTICLE = "https://www.cnn.com/2020/10/13/politics/supreme-court-census/index.html"
file = urllib.request.urlopen(NEWS_ARTICLE)
for line in file:
  decoded_line = line.decode("utf-8")

print(decoded_line)
