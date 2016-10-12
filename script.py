import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/in/garvit-joshi-5b4804a8"
urlopener= urllib.request.build_opener()
urlopener.addheaders = [('User-agent', 'Mozilla/5.0')]
page = urlopener.open(url).read()
soup = BeautifulSoup(page,"html.parser")
tweets = soup.findAll('section', {'class':'profile-section'})
#for i in tweets:
print(tweets.text)
	print("\n")
