import re
import string

# synartisi pou vriskei lekseis apo mikos a ews b (Ara to result den tha exei lekseis mikous 20)
def find_words(a, b, s):

    result = []

    lines = s.splitlines()

    for line in lines:

        l = "".join([char for char in line if char not in string.punctuation])


        find = [token for token in l.split(" ") if a <= len(token) <= b]


        result += find

    return result

# Anoigma arxikou arxeiou, afairesi eidikwn xaraktirwn kai arithmwn, eggrafi apotelesmatos se neo arxeio

strings = open('two_cities_ascii.txt').read()
new_str = re.sub('[^a-zA-Z\n]', ' ', strings)
open('new.txt', 'w').write(new_str)

#Anoigma neou arxeiou gia eksagwgi statistikwn

file =open('new.txt')
lines=file.readlines()
res=[]    
for l in lines:
    res.append(find_words(1,19,l))


size=int(input("Enter a number between 1-19 to view how many words have this size:"))
counter=0
for data in res:
    for l in data:
        if len(l)==size:
            counter+=1
print("%d words with size %d" %( counter,size))            