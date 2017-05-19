import shelve

shelfFile = shelve.open('mydata')
list(shelFile.keys())

list(shelFile.values())

shelFile.close()
