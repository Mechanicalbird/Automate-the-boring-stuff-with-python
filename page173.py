import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = sxampleSoupe.select('#author')
print(type(elems))
print(len(elems))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
