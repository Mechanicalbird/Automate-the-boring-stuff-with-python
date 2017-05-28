import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endwith('#'):
    # download the image
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # find the URL of the image
    comicElem == soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         comicUrl = comicElem[0].get('src')
         print('Downloading image %s...' % (comicUrl))
         res = requests.get(comicUrl)
         res.raise_for_status()

    # save the image

    # to Prev button



print('Done.')
