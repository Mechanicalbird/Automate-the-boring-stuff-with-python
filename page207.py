import pprint
cats = [{'name': 'zophie', 'desc':'chubby'}, {'name':'pooka', 'desc':'fluffy'}]
pprint.pformat(cats)
print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
