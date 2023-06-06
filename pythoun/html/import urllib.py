import urllib.request

url = "https://www.nate.com"
res =  urllib.request.urlopen(url)
#html = res.read()

bs0bject = bs4.BeautifulSoup(res,'html.parser')

print(bs0bject)