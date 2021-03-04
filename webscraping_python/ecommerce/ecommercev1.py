import requests
import os.path
import json
from lxml import html

def processingEngine(url,no_of_results,output):
    product = html.fromstring(url.content)
    product_title = product.xpath('//strong[@class="product name product-item-name"]//a/text()')
    product_link = product.xpath('//a[@class="product-item-link"]/@href')
    product_retail_price = product.xpath('//span[@class="old-price"]//@data-price-amount')
    product_dicounted_price = product.xpath('//span[@class="special-price"]//@data-price-amount')

    if not product_title and len(product_title)==0:
        print("Enter a Valid Search Term")
    else:
        for i in zip(product_title,product_link,product_retail_price,product_dicounted_price):
            dic = {}
            dic['Title']=i[0]
            dic['Link']=i[1]
            dic['Retail']=i[2]
            dic['Discounted']=i[3]
            output.append(dic)

        product_next_page=product.xpath('//li[@class="item pages-item-next"]/a[@class="action  next"]/@href ')
        if product_next_page and len(output) < no_of_results:
            url1 = requests.get("https://www.afsupply.com/catalogsearch/result/?q="+product_next_page[0])
            processingEngine(url1, no_of_results, output)
        elif len(output)>no_of_results:
            pass
        else:
            print("Results are less than asked for")
            print("Printing available results",len(output))

def inputEngine(user_input,no_of_results,outpput):
    url=requests.get("https://www.afsupply.com/catalogsearch/result/?q="+user_input)
    processingEngine(url,no_of_results,outpput)

user_input=input("Enter the Product you Want : ")
no_of_results=100 #int(input("Enter results you Want : "))
output=[]
inputEngine(user_input,no_of_results,output)
ans=output[:no_of_results]
json_obj=json.dumps(ans,indent=4)

with open('inventory.txt','w') as f:
    f.write(json_obj)



# save_path=r'/Users/chetan.sirohi/PycharmProjects/sample/ecommerce'
# complete_path=os.path.join(save_path,user_input+'.html')
#
# with open(complete_path,'w') as f:
#     f.write(url.text)
#
# with open(complete_path,'r' ) as f:
#     parsing_url=f.read()


