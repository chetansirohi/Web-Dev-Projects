import json
import requests
from lxml import html

url='https://www.canadiantire.ca/en/search-results.html?q=cycle'
agent = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}
page = requests.get(url, headers=agent)
# print(page.content)

api_get=requests.get('https://api.canadiantire.ca/search/api/v0/product/en/?site=ct;store=0452;format=json;count=36;q=cycle').json()
output=[]
for i in api_get['results']:
    output.append(i["field"])
    # output.append({"product id":i['prod-id'],"Product sku":i["sku-id"],"url":'https://www.canadiantire.ca'+i["short-pdp-url"]})

real_op=[]
for i in output:
    real_op.append({"Product Name":i['prod-name'],"SKU":i["sku-id"],"URL":'https://www.canadiantire.ca'+i["short-pdp-url"]})

# print(real_op)

json_obj=json.dumps(real_op,indent=4)
with open('ecom2.txt','w') as f:
    f.write(json_obj)

# for i in output:
#     print(i["field"])

# print(api_get.json())

# json_obj=json.dumps(api_get.json(),indent=4)
# with open('ecom2.txt','w') as f:
#     f.write(json_obj)
#
# json_obj1=json.loads(json_obj)
# # print(json_obj1["results"])
#
# output=[]
# for i in json_obj1["results"]:
#     output.append(i.values())
# print(output[0])



