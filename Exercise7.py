# importing the module
import json

file=open('dictionary.txt','r')
data=file.read()
dat=json.loads(data)


for i in dat:
   keys_list=list(i.keys())

print("Available keys:")
for i in keys_list:
    print(i, end=" ")
    if i=='name':
        print('\n',end='')
maxEl=0
minEl=0
ch=""

key=input("Select a key to view info:")
if key in keys_list:
    for d in dat:
        if key == 'name':
            if d.get(key)>ch:
                maxEl=d.get(key)
            elif d.get(key)<maxEl:
                minEl=d.get(key)
        else:
            if d.get(key)>maxEl:
                maxEl=d.get(key)
            elif d.get(key)<minEl:
                minEl=d.get(key)

print("Maximum element of selected key is: ",maxEl)
print("Minimum element of selected key is: ",minEl)            

