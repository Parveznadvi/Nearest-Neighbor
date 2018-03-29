## K-NEAREST-NEIGHBOR ALGORITHM

from math import sqrt
import numpy as np
from operator import itemgetter
from heapq import nsmallest
from collections import Counter

train= open ("train.txt","r")
test=open ("test.txt","r")
cor=0
wor=0
ind=-1
trg=[]
tsg=[]
a=[]
k=int(input("Enter the value of k:"))
knn=[]

for line in train :
    trg+=[line.split(',')]
for line in test :
    tsg+=[line.split(',')]
w=len(trg[0])-1

for i in range(len(trg)):
    a+=[i]

def kmin(dist):
    global k
    lb=[]
    pairs=zip(a,dist)
    result = nsmallest(k, pairs, key=itemgetter(1))
    #print(result)
    knn = [ i[0] for i in result ]
    for i in range(len(knn)):
        lb+=[trg[knn[i]][w]]
    kn=Counter(lb).most_common()
    return (kn[0][0])
    #return knn 
   
    
for x in range(0,len(tsg)):
    mindist=100
    dist=[]
    for y in range(0,len(trg)):
        ##print(tsg[x][0],tsg[x][1],tsg[x][2],tsg[x][3])
        ##print(trg[y][0],trg[y][1],trg[y][2],trg[y][3])
        dst=((float(tsg[x][0])-float(trg[y][0]))**2)\
             +((float(tsg[x][1])-float(trg[y][1]))**2)\
             +((float(tsg[x][2])-float(trg[y][2]))**2)\
             +((float(tsg[x][3])-float(trg[y][3]))**2)
        dst=sqrt( dst)
        dist+=[dst]
    print()
    knn=kmin(dist)
    #print(knn)    
    inde=int(x)
    t=tsg[inde][w]
    if t==knn:
        print ("Correct")
        print(t,knn)
        cor+=1
    else:
        print("Wrong")
        print(t,knn)
        wor+=1
    print ("--------------------")
    print()

print()
print("Number of training patterns =",len(trg))
print("Number of test patterns =",len(tsg))
print("Correctly classified =",cor)
print("Incorrectly classified =",wor)
n=len(tsg)
ca=((cor/n)*100)
print("Correct Accuracy=",ca)
