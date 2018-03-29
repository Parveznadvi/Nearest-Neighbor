## NEAREST-NEIGHBOR ALGORITHM

from math import sqrt
import numpy as np

train= open ("cndd.txt","r")
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
w=3
dist=[]

for line in train :
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

for x in range(0,len(tsg),4):
    mindist=100
    dist=[]
    for y in range(0,len(trg),4):
        #print(tsg[x],tsg[x+1],tsg[x+2],tsg[x+3])
        #print(trg[y],trg[y+1],trg[y+2],trg[y+3])
        dst=(((tsg[x]-trg[y])**2)+((tsg[x+1]-trg[y+1])**2)+((tsg[x+2]-trg[y+2])**2)+((tsg[x+3]-trg[y+3])**2))
        dst=sqrt( dst)
        dist+=[dst]
        ##print(dst)
        ##print()
    print("********************")
    for i in range(len(dist)):
        if mindist>dist[i]:
            mindist=dist[i]
            ind=i
    print("mindist=",mindist,"\nindex=",ind)
    inde=int(x/4)
    if tsl[inde]==trl[ind]:
        print ("Correct")
        print(inde,ind)
        cor+=1
    else:
        print("Wrong")
        print(inde,ind)
        wor+=1
    print ("--------------------")
    print()
    
print()
print("Number of training patterns =",htr)
print("Number of test patterns =",hts)
print("Correctly classified =",cor)
print("Incorrectly classified =",wor)
n=len(tsl)
ca=(cor/n)*100
print("Correct Accuracy=",ca)