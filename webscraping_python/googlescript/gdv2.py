import requests
from lxml import html
import json

def fetchTitlesUrls(user_input):
    #get the results for the mentioned term
    url=requests.get('https://www.google.com/search?q='+user_input)

    #build xpath tree
    tree=html.fromstring(url.content)
    #############Conditions#########
    ## 1. User Enter the Correct Term
    ## 2. User Enter the Incorrect Term but is still shown/redirected to Correct Results
    ## 3. User Enter Completely Different Term and is shown the Results of the Entered Term
    ## 4. User Enter an Invalid Term that does not fetch any results and Gives a message to the user that it did not fetch any results


    #Checking the Conditons
    #Tree Titles or Search Results Title
    tree_title=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//div[@class="BNeawe vvjwJb AP7Wnd"]//text()')

    #Tree Urls or Search Results URLs
    tree_links=tree.xpath('//div[@class="kCrYT"]//h3[@class="zBAuLc"]//parent::a/@href')

    #cleaning Urls to redirect to correct webpage  ###To be Optimized
    cl_url=[]
    for i in tree_links:
        # if 'twitter' in i:
        #     cl_url.append(i[7:].replace('%3Fre',' ').split()[0])
        # elif 'amazon' in i:
        #     az=(i[7:].replace('b%3Fie', ' ').split()[0])
        #     cl_url.append(az.replace("%",""))
        # else:
        cl_url.append(i.replace('/url?q=',"").replace('&sa'," ").replace("%3F","?").replace("%3D","=").split()[0])
    # print(tree_links.replace('&sa'," ").split()[0])

    if not tree_title:
        print("enter valid keywords")
    else:
        output=[]
        for i in zip(tree_title,cl_url):
            res={}
            res["Title"]=i[0]
            res["Link"]=i[1]
            output.append(res)
    json_obj=json.dumps(output,indent=4)
    with open("results.txt","a") as f:
        f.write(json_obj)


#enter the term you want to search
user_input=input("Enter the Search Term you want : ")
fetchTitlesUrls(user_input)

# enter how many results you want to search
# no_of_results=int(input("Enter how many Search Results you want : "))
