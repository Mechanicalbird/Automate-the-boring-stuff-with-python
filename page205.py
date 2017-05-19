import shelve

shelfFile = shelve.open('mydata')
cats = ['zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close

