import json
import requests
from lxml import html

def pdtInfo(url1):
    pdt_det=[]
    pdt_nfo=html.fromstring(url1.content)
    pdt_pg=pdt_nfo.xpath('//div[contains(@class,"product-info-price")]')
    for i in pdt_pg:
        dic={}
        dic["SKU"]=i.xpath('.//div[contains(@class,"sku")]/div[@class="value"]//text()')[0]
        dic["Availibility"]=i.xpath('.//p/span/text()')[0]
        dic["Retail Price"]=i.xpath('.//span[contains(@id,"old-price")]//text()')[0]
        dic["Special Price"]=i.xpath('.//span[contains(@id,"product-price")]//text()')[0]
        pdt_det.append(dic)
    return pdt_det

def processingEngine(url,no_of_results,output):
    pdt_cntnt=html.fromstring(url.content)
    pdt=pdt_cntnt.xpath('//ol[contains(@class,"product-items")]//li[contains(@class,"product-item")]')
    for i in pdt:
        dic={}
        dic['Title']=i.xpath('.//strong//text()')[0]
        dic['Link']=i.xpath('./div/a/@href')[0]
        dic["Product Details"]=pdtInfo(requests.get(i.xpath('./div/a/@href')[0]))

        output.append(dic)

    product_next_page = pdt_cntnt.xpath('//li[@class="item pages-item-next"]/a[@class="action  next"]/@href ')
    if product_next_page and len(output) < no_of_results:
        url1 = requests.get("https://www.afsupply.com/catalogsearch/result/?q=" + product_next_page[0])
        processingEngine(url1, no_of_results, output)
    elif len(output) > no_of_results:
        pass
    else:
        print("Results are less than asked for")
        print("Printing available results", len(output))

def inputEngine(user_input,no_of_results):
    output=[]
    url=requests.get("https://www.afsupply.com/catalogsearch/result/?q="+user_input)
    processingEngine(url,no_of_results,output)
    return output

user_input=input("Enter the Search Term : ")
no_of_results=int(input("Enter How many Results : "))
ans=inputEngine(user_input,no_of_results)
res=ans[:no_of_results]

json_obj=json.dumps(res,indent=4)
with open('inventory.txt','w') as f:
    f.write(json_obj)

