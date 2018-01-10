# -*- coding: cp1252 -*-
import unittest
<<<<<<< HEAD
import urllib2

def takeSecond(elem):
    return elem[1]

page = urllib2.urlopen('http://www.unisport.dk/api/sample/')
pagedata = page.read()

data = pagedata.split("{")

dictlist = []
dictcount = 0
#print "boop"
for datapoint in data:
    #print "boop"
    if dictcount >= 2:
        data2 = datapoint.split("\"")
        #print "boop"
        #print data2
        data2 =[e for e in data2 if e not in ('', ' ', ', ', ': ', '}, ')]

        datadict = dict(zip(data2[::2], data2[1::2]))
        #print datadict
        dictlist.append(datadict)
    #else:
        #print datapoint
    dictcount = dictcount + 1
#print "boop"

cheaplist = []
for product in dictlist:
    cheaplist.append([product['name'], product['price']])

cheaplist.sort(key=takeSecond)


#Number one
print "Cheap List"
print cheaplist[0:10]

cheaplist = []

#number 2
#'kids' har kun 0-værdier. jeg antager at der menes 'kid_adult' i opgaven,
# da der er en blanding af 0 og 1 værdier.

for product in dictlist:
    if product['kid_adult'] == '1':
        cheaplist.append([product['name'], product['price']])

cheaplist.sort(key=takeSecond)

print "For Kids cheap List"
print cheaplist[0:10]




=======
gfdhfd
>>>>>>> origin/master
