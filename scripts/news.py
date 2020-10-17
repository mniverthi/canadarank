import requests

# some query parameters
country = 'ca'
api_key = '40ac3cd1f8344ea19a5bd055f75ba17c'
num_results = 100

# http url
url1 = "http://newsapi.org/v2/everything?q=Trump&from=2020-10-14&to=2020-10-16&apiKey={}".format(api_key)
url2 = "http://newsapi.org/v2/top-headlines?country={}&pageSize={}&apiKey={}".format(country, num_results, api_key)

# response object
response = requests.get(url2)
print("status code:", response.status_code)
response = response.json()
print("num results:", response['totalResults'])

articles = response['articles']
article_str = ""
for article in articles:
    source = article['source']
    url = article['url']
    article_str += (url + "\n")

f = open('articles.txt', 'a')
f.write(article_str)
f.close()
