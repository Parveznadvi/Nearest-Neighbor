## NEAREST-NEIGHBOR ALGORITHM

from math import sqrt
import numpy as np

train= open ("3.txt","r")
test=open ("4.txt","r")
trg=[]
tsg=[]

for line in train :
    trg+=[line.split(',')]
for line in test :
    tsg+=[line.split(',')]
w=len(trg[0])-1

for x in range(0,len(tsg)):
    mindist=100
    dist=[]
    bist=[]
    for y in range(0,len(trg)):
        bst=0
        ##print(tsg[x][0],tsg[x][1],tsg[x][2],tsg[x][3])
        ##print(trg[y][0],trg[y][1],trg[y][2],trg[y][3])
        dst=sqrt(((float(tsg[x][0])-float(trg[y][0]))**2)\
             +((float(tsg[x][1])-float(trg[y][1]))**2)\
             +((float(tsg[x][2])-float(trg[y][2]))**2)\
             +((float(tsg[x][3])-float(trg[y][3]))**2))
        dist+=[dst]

        for i in range(0,w):
            bst+=((float(tsg[x][i])-float(trg[y][i]))**2)
        bst=sqrt( bst)
        bist+=[bst]
        

