import requests
from  lxml import html

user_input=input("Enter your Input : ")

url=requests.get('https://www.google.com/search?q='+user_input)
# print(url.content)

tree=html.fromstring(url.content)

tree_title=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')

# for i,j in zip(tree_title,tree_links):
#     while True:
#         with open('results.txt','w' ) as f:
#             f.write(f'Title : {i}\n')
#             f.write(f'Link : {j[7:]}')
#         b

for i in range(len(tree_title)):
    with open('results.txt','a') as f:
        f.write(f'Title : {tree_title[i]}\n')
        f.write(f'Link : {tree_links[i]}\n\n')
