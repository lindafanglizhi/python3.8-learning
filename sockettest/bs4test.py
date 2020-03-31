from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.baidu.com")
bsobj = BeautifulSoup(html.read(), "lxml")
# print(bsobj.body)
all = bsobj.findAll(id="kw")
print(all)
