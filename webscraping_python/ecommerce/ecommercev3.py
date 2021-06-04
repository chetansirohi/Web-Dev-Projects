import json
import requests
from lxml import html,etree

def jsonToDict(jsfrmt):
    url_li=[]
    res = json.loads(jsfrmt)  # converts json data to python dictionary
    # print(res["offers"]) #returns the list of product details from the converted string dictionary
    for i in res["offers"]:
        if i["availability"].split('/')[-1].lower()== "instock":
            url_li.append(i["url"])

    return url_li

def instockPdtDets(ins_url,output):
    for i in ins_url:
        url=requests.get(i)
        pdt_det=html.fromstring(url.content)
        pdt_xp=pdt_det.xpath('//div[contains(@class,"lastColumn")]')
        for j in pdt_xp:
            dic={}
            dic["Title"] = j.xpath('.//h1//text()')[0]
            dic["URL"] = i
            dic["SKU"] = j.xpath('.//div[@class="productVariations"]/@data-master-id')[0]
            if j.xpath('.//p[contains(@class,"rrp")]//text()'):
                dic["Retail Price"] = j.xpath('.//p[contains(@class,"rrp")]//text()')[0]
            dic["Discounted Price"] = j.xpath('.//p[@data-product-price="price"]/text()')[0].replace("\n", "")
            labels=[k.replace("\n","").strip() for k in j.xpath('.//label[@class="productVariations_dropdownLabel"]//text()')]
            if "Color" in labels:
                dic["Color"]=j.xpath('.//select[@id="product-variation-dropdown-2"]//option[@selected]/text()')[0].replace("\n","")
            if "Size" in labels:
                dic["Size"] = j.xpath('.//span[@class="srf-hide"]//parent::button//text()')[0].replace("\n", "")
            if "Option" in labels:
                dic["Option"] = j.xpath('.//select[@id="product-variation-dropdown-10"]//option[@selected]/text()')[0].replace("\n", "")
            if "Flavor" in labels:
                dic["Flavor"]=j.xpath('.//select[@id="product-variation-dropdown-5"]//option[@selected]/text()')[0].replace("\n", "")
            if "Amount" in labels:
                dic["Amount"]=j.xpath('.//select[@id="product-variation-dropdown-7"]//option[@selected]/text() ')[0].replace("\n", "")

            output.append(dic)

    return output


def productSims(url,output):
    product=html.fromstring(url.content)
    pdt_json=product.xpath('//script[contains(@type,"json")][1]//text()')[0]
    ins_url=jsonToDict(pdt_json)
    result=instockPdtDets(ins_url,output)
    json_obj=json.dumps(result,indent=4)
    with open('ecom2.txt','w') as f:
        f.write(json_obj)

url=requests.get("URL")
output=[]
productSims(url,output)


