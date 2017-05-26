import requests, bs4
res = requests.get('https://www.nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
print(type(noStarchSoup))
