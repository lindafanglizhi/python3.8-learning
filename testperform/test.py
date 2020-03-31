import requests
import json
import urllib.request
import datetime

for i in range(1,210):
    print("当前正在抓取第",i,"页")
    now1 = datetime.datetime.now()
    # url = "http://47.98.53.254:19999/wall/?page=%d"%i
    url = "http://47.98.53.254:19999/getPic/?page=%d"%i
    response = requests.get(url)
    print(response.elapsed.total_seconds());
    result_str = response.text
    result_json = json.loads(result_str)
    for image_name in result_json["data"]:
        image_url = "http://47.98.53.254:19999/static/"+image_name
        urllib.request.urlretrieve(image_url, "images/"+image_name)

    total_time = datetime.datetime.now()-now1;
    print(total_time);
