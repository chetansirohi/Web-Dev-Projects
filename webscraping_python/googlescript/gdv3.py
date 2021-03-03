import requests
from lxml import html
import json

def processingEngine(url,no_of_results,output):
    tree=html.fromstring(url.content)
    tree_title = tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
    tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')

    cl_url = []
    for i in tree_links:
        cl_url.append(i.replace('/url?q=', "").replace('&sa', " ").replace("%3F", "?").replace("%3D", "=").split()[0])

    if not tree_title and len(tree_title)==0:
        print("Enter valid keywords and No Results Found")
    else:
        for i in zip(tree_title, cl_url):
            res = {}
            res["Title"] = i[0]
            res["Link"] = i[1]
            output.append(res)
        new_page = tree.xpath('//a[@aria-label="Next page"]/@href')
        if new_page and len(output) < no_of_results:
            url1 = requests.get("https://www.google.com" + new_page[0])
            processingEngine(url1, no_of_results, output)
        elif len(output)>no_of_results:
            pass
        else:
            print("Results are less than asked for")
            print("Printing available results",len(output))





def inputEngine(user_input,no_of_results,output):
    url=requests.get("https://google.com/search?q="+user_input)
    processingEngine(url,no_of_results,output)

user_input=input("Enter Search Term : ")
no_of_results=int(input("Enter No of Results Wanted : "))
output=[]
inputEngine(user_input,no_of_results,output)
ans=output[:no_of_results]
json_obj = json.dumps(ans, indent=4)
with open("results.txt", "w") as f:
    f.write(json_obj)



# def ip(user_input,no_of_results,output):
#     url=requests.get("https://www.google.com/search?q="+user_input)
#     inputO(url,no_of_results,output)
#
# def inputO(url,no_of_results,output):
#     tree=html.fromstring(url.content)
#     tree_title = tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
#     tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')
#
#     cl_url=[]
#     for i in tree_links:
#         cl_url.append(i.replace('/url?q=',"").replace('&sa'," ").replace("%3F","?").replace("%3D","=").split()[0])
#
#     if not tree_title:
#         print("Enter valid keywords")
#     else:
#         for i in zip(tree_title,cl_url):
#             res={}
#             res["Title"]=i[0]
#             res["Link"]=i[1]
#             output.append(res)
#     print(len(output))
# ########### take care of edge cases here
#
#     if not tree_title:
#         print("No Results Found")
#     else:
#         if len(output)<=no_of_results:
#             new_page = tree.xpath('//a[@aria-label="Next page"]/@href')
#             url1 = requests.get("https://www.google.com" + new_page[0])
#             inputO(url1,no_of_results,output)
#
#
#
# user_input=input("Enter the Search Term : ")
# no_of_results=int(input("Enter No of Results : "))
# output=[]
# ip(user_input,no_of_results,output)
# ans=output[:no_of_results]
# json_obj = json.dumps(ans, indent=4)
# with open("results.txt", "w") as f:
#     f.write(json_obj)



# def newPage(url,tree):
#
#     tree_title = tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
#     tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')
#
#     cl_url=[]
#     for i in tree_links:
#         cl_url.append(i.replace('/url?q=',"").replace('&sa'," ").replace("%3F","?").replace("%3D","=").split()[0])
#
#     if not tree_title:
#         print("enter valid keywords")
#     else:
#         for i in zip(tree_title,cl_url):
#             res={}
#             res["Title"]=i[0]
#             res["Link"]=i[1]
#             output.append(res)




# def processingEngine(url,output):
#     tree=html.fromstring(url.content)
#     tree_title = tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
#     tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')
#     # while len(output)<no_of_results:
#     #     next_page = tree.xpath('//a[@aria-label="Next page"]/@href')
#     #     processingEngine("https://www.google.com"+next_page[0],output)
#     outputEngine(tree_title,tree_links,output)
#
#
# def outputEngine(tree_title,tree_links,output):
#     cl_url=[]
#     for i in tree_links:
#         cl_url.append(i.replace('/url?q=',"").replace('&sa'," ").replace("%3F","?").replace("%3D","=").split()[0])
#
#     if not tree_title:
#         print("enter valid keywords")
#     else:
#
#         for i in zip(tree_title,cl_url):
#             res={}
#             res["Title"]=i[0]
#             res["Link"]=i[1]
#             output.extend(res)
#
# def inputEngine(user_input,no_of_results):
#     output=[]
#     url=requests.get("https://www.google.com/search?q="+user_input)
#     processingEngine(url,output)
#     print(output)
#
# user_input=input("Enter Search Term : ")
# no_of_results=int(input("Enter the no of results : "))
# inputEngine(user_input,no_of_results)


# def nextpage(url):
#     tree=html.fromstring(url.content)
#     tree_title = tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
#     tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')
#     return tree_title,tree_links

#
# def fetchTitlesUrls(user_input):
#     url=requests.get('https://www.google.com/search?q='+user_input)
#     tree=html.fromstring(url.content)
#     tree_title=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')
#     tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')
#     next_page=tree.xpath('//a[@aria-label="Next page"]/@href')
#     cl_url=[]
#     for i in tree_links:
#         cl_url.append(i.replace('/url?q=',"").replace('&sa'," ").replace("%3F","?").replace("%3D","=").split()[0])
#
#
#     if not tree_title:
#         print("enter valid keywords")
#     else:
#         output=[]
#         for i in zip(tree_title,cl_url):
#             res={}
#             res["Title"]=i[0]
#             res["Link"]=i[1]
#             output.append(res)
#     print(next_page)
#
#     #
#     # json_obj = json.dumps(output, indent=4)
#     # with open("results.txt", "a") as f:
#     #     f.write(json_obj)
#     # for i in range(len(output)):
#     #     print(output[i])
#     print(output)
#
# user_input=input("Enter the Search Term you want : ")
# fetchTitlesUrls(user_input)
# no_of_results=int(input("Enter how many Search Results you want : "))
