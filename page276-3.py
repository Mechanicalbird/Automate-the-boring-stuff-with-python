#! python3
# luucky.py - opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
#res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://www.google.co.jp/search?q=SEARCH_TERM_HERE&gws_rd=cr&ei=hOMqWbagAoGu0ASdorHICw')

res.raise_for_status()

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result.

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print(webbrowser.open('http://google.com' + linkElems[i].get('href')))

