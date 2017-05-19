import shelve

shelfFile = shelve.open('mydata')
type(shelfFile)

shelFile['cats']

shelFile.close()
