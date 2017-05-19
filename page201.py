import os
os.getcwd()
print(os.getcwd())

size=os.path.getsize('/home/mechanicalbird/Desktop/General-Learning/Automate/old/page89.py')
print(size)

listall = os.listdir('/home/mechanicalbird/Desktop/General-Learning/Automate/old')

print(listall)

totalSize =0

path = '/home/mechanicalbird/Desktop/General-Learning/Automate/old'

for filename in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path , filename))

statment = 'totalSize ='
print(str(statment) + str(totalSize))
