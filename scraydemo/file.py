import requests

header ={
    'user_agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url="https://petstore.swagger.io/v2/pet/1"

r=requests.get(url=url)
print(r.json())
print(r.status_code)
print(r.text)
print(r.json()['message'])


