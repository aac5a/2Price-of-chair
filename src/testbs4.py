import requests, bs4

res = requests.get('http://nostarch.com/')
try:
    res.raise_for_status()
except Exception as exc:
    print("nie pobralem: %s \n!!!" % (exc))
#print(type(res))
res = res.content
#print(type(res))
#print(res)
noStarchSoup = bs4.BeautifulSoup(res, "html.parser")
print(str(noStarchSoup)+ "\n \n duupa")