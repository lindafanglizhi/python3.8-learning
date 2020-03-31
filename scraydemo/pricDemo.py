import requests
import json
import urllib.request

headers = {
'user_agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
for i in range(1,2):
    print("当前正在抓取第",i,"页")
    url = "http://47.98.53.254:29999/getPic/?page=%d"%i
    response = requests.get(url,headers=headers)
    result_str = response.text
    result_json = json.loads(result_str)
    for image_name in result_json["data"]:
        image_url = "http://47.98.53.254:29999/static/"+image_name
        image_url = image_url.replace(' ','%20')
        print(image_url)

        with open(image_url, "wb") as code:
            code.write()
        urllib.request.urlretrieve(image_url,"/Users/lindafang/PycharmProjects/scraydemo/images/"+image_name)
