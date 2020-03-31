import requests

class tt(object):
    def get_pet(self):
        url='https://petstore.swagger.io/v2/pet/1'
        req = requests.get(url=url)
        print(req.status_code)
        print(req.json())


a=tt()
a.get_pet()


