import json
import requests
from lxml import html


def inputEngine(url,noOfIp,output):
    pdt = html.fromstring(url.content)
    # pdt_xp = pdt.xpath('//div[@class="products wrapper grid products-grid columns4"]')
    nextpg=pdt.xpath('//a[@title="Next"]//@href')
    pid=pdt.xpath('//div[@class="products wrapper grid products-grid columns4"]//@product-id')
    for i in pid:
        dic={}
        dic["Title"]=pdt.xpath('//div[@product-id='+str(i)+']//span[@class="inner-description"]//following-sibling::a/@title')[0]
        dic["URL"]=pdt.xpath('//div[@product-id='+str(i)+']//strong//@href')[0]
        dic["SKU"]=pdt.xpath('//div[@product-id='+str(i)+']//span[@itemprop="sku"]//text()')[0]
        output.append(dic)
    if len(output)<noOfIp:
        url1=requests.get('https://www.familyfarmandhome.com'+nextpg[0])
        inputEngine(url1,noOfIp,output)
    return output


url=requests.get("https://www.familyfarmandhome.com/catalogsearch/result/usb")
output=[]
noOfIp=40
ans=inputEngine(url,noOfIp,output)
json_obj=json.dumps(ans,indent=4)

with open('ecom2.txt','w') as f:
    f.write(json_obj)
