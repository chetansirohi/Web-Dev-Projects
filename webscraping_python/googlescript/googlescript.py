import requests
from lxml import html
import os.path

user_input=input("Enter What do you want to Search : ")

url=requests.get('https://www.google.com/search?q='+user_input)
# print(url.content)

save_path=r'/Users/chetan.sirohi/PycharmProjects/sample/googlescript'
compelte_path=os.path.join(save_path,user_input+'.html')

# with open(compelte_path,"w") as f:
#     f.write(url.text)

with open(compelte_path,"r") as f:
    parsing_url=f.read()

# parsing_url='http://localhost:63342/sample/googlescript/nike.html?_ijt=uanmvq9gdaqt68928i9b7752si'
#
tree=html.fromstring(parsing_url)
# tree_title=tree.xpath('//div[@id="main"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
# print(tree_title)

# for tree_title in tree.xpath('//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()'):
#     print(tree_title)

tree_title=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')
#
# print("Length of Titles List : ",len(tree_title))
# print("Length of URLs List : ",len(tree_links))
#
# for tree_title in tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()'):
#     print(tree_title)

# tree_links=tree.xpath('//div[@id="main"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//parent::h3//parent::a')

# for tree_links in tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href'):
#     print(tree_links)

# for _ in tree:
#     print(tree.xpath('//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()'))
#     print(tree.xpath('//h3[@class="zBAuLc"]//parent::a'))

dic={}
for i in range(len(tree_title)):
    dic[tree_title[i]]=tree_links[i]

print(dic)
