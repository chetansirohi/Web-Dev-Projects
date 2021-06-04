#https://towardsdatascience.com/how-to-use-python-and-xpath-to-scrape-websites-99eaed73f1dd
import requests
from urllib.request import urlopen
from lxml import etree

url='https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
headers={'Content-Type':'text/html'}
response=requests.get(url,headers=headers)
html=response.text

with open('star_wars_html','w') as f:
    f.write(html)

local='file:///Users/chetan.sirohi/PycharmProjects/sample/star_wars_html.html'
response=urlopen(local)
htmlparser=etree.HTMLParser()
tree=etree.parse(response,htmlparser)

for quote in tree.xpath('//p/strong/text()'):
    print(quote) #prints the quotes
print(tree.xpath('//p/strong[not(contains(text(),"\xa0"))]/text()')) #Print the infor below the quote
print(tree.xpath('//img[starts-with(@class,"alignnone")]/@src'))#gives the image url
    # print(tree.xpath('//header[@class="article header"]/descendant::node()/text()')) #fetches all metadata
print(tree.xpath('//li[@class="related-post"]/a[1]/@href')) #fetches urls of related posts

