from bs4 import BeautifulSoup
import requests
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

tweetArray = []
for tweet in content.findAll('div', attrs={"class":
                                              "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "content": tweet.find('p', attrs={"class": "content"}).text,
        "dateTime": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweetArray.append(tweetObject)
    with open('tweerData.json', 'w') as outfile:
        json.dump(tweetArray, outfile)
