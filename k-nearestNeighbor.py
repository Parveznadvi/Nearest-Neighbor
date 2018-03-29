## K-NEAREST-NEIGHBOR ALGORITHM

from math import sqrt
import numpy as np
from operator import itemgetter
from heapq import nsmallest

train= open ("train.txt","r")
test=open ("test.txt","r")
cor=0
wor=0
ind=-1
trg=[]
trl=[]
tsg=[]
tsl=[]
htr=0
hts=0
x=0
y=0
w=4
dist=[]
cn=0
a=[]
k=int(input("Enter the value of k:"))
      
for line in train:
    x1,x2,x3,x4,x5=line.split(',')
    trg+=([x1,x2,x3,x4])
    trl+=[x5]
    htr+=1
for line in test :
    y1,y2,y3,y4,y5=line.split(',')
    tsg+=([y1,y2,y3,y4])
    tsl+=[y5]
    hts+=1
trg=np.array(trg,dtype=np.float64)
tsg=np.array(tsg,dtype=np.float64)

for i in range(len(trl)):
    a+=[i]
##print(a)
mindist=[]
ind=[]
i=0
for x in range(0,len(tsg),4):
    mindist=100
    dist=[]
    
    for y in range(0,len(trg),4):
        ##print(tsg[x],tsg[x+1],tsg[x+2],tsg[x+3])
        ##print(trg[y],trg[y+1],trg[y+2],trg[y+3])
        dst=(((tsg[x]-trg[y])**2)+((tsg[x+1]-trg[y+1])**2)+((tsg[x+2]-trg[y+2])**2)+((tsg[x+3]-trg[y+3])**2))
        dst=sqrt( dst)
        dist+=[dst]
        pairs=zip(a,dist)   
    print()
    result = nsmallest(k, pairs, key=itemgetter(1))
    id = [ i[0] for i in result ]
    ##print(result)
    print(id)
    ##print()         

    inde=int(x/4)
    for i in range(len(id)):
        if tsl[inde]==trl[id[i]]:
            print ("Correct")
            print(inde,id[i])
            cor+=1
        else:
            print("Wrong")
            print(inde,id[i])
            wor+=1
    print ("--------------------")

print("Number of training patterns =",htr)
print("Number of test patterns =",hts)
print("Correctly classified =",cor)
print("Incorrectly classified =",wor)
ca=((cor/hts)*100)/k
print("Correct Accuracy=",ca)


##tsg=np.matrix(tsg)
##trg=np.matrix(trg)
##print(tsg.shape)
##print(trg.shape)
##print(trg.dtype)
##print (trg[3])
##print(tsg.shape)
##print(tsg.dtype)
##print (tsg[0])
##print(tsg[19]-trg[19])
##print(htr,hts)

##print(len(dist))
##print(len(tsl))
##print(len(trl))

##print("Train dataset")
##print (trg)
##print (trl)
##print("Test dataset")
##print (tsg)
##print (tsl)

##for x in range(0,len(tsg),4):
##    print(tsg[x],tsg[x+1],tsg[x+2],tsg[x+3])
##print()
##for y in range(0,len(trg),4):
##    print(trg[y],trg[y+1],trg[y+2],trg[y+3])
