## CONDENSED NEAREST-NEIGHBOR ALGORITHM
import numpy as np
from math import sqrt

train = open ("train.txt","r")
out=open("cnddd.txt","w")
trg=[]
cd=[]
rd=[]
dst=[]
ind=-1
cor=0
wor=0
string=""

for line in train :
    trg+=[line.split(',')]
w=len(trg[0])-1

cd = [trg[0]]
##def red(trg,cd):
##    rd = set(tuple(x) for x in trg ).difference(tuple(x) for x in cd)
##    rd = list(rd)
##    rd=sorted(rd)
##    return rd
##rd=red(trg,cd)
rd=[x for x in trg if x not in cd]

def calc(rd,cd):
    
    for x in range(0,len(rd)):
        mindist=100
        dist=[]
        for y in range(0,len(cd)):
            ##print(rd[x][0],rd[x][1],rd[x][2],rd[x][3])
            ##print(cd[y][0],cd[y][1],cd[y][2],cd[y][3])
            dst=((float(rd[x][0])-float(cd[y][0]))**2)\
                 +((float(rd[x][1])-float(cd[y][1]))**2)\
                 +((float(rd[x][2])-float(cd[y][2]))**2)\
                 +((float(rd[x][3])-float(cd[y][3]))**2)
            dst=sqrt( dst)
            dist+=[dst]
            ##print(dst)
            ##print()
        #print("********************")
        for i in range(len(dist)):
            if mindist>dist[i]:
                mindist=dist[i]
                ind=i
        ##print("mindist=",mindist,"\nindex=",ind)
        inde=int(x)
        if rd[inde][w]==cd[ind][w]:
            #print ("Correct")
            #print(inde,ind)
            ##rd=red(rd,cd)
            continue
        else:
            #print("Wrong")
            #print(inde,ind)
            cd+=[rd[inde]]
            ##rd=red(rd,cd)
        #print ("--------------------")
        #print()
            
tracker =0
calc(rd,cd)
#print(np.array(cd),"\n")
while tracker!=len(cd):
    tracker = len(cd)
    calc(rd,cd)
    #print(np.array(cd),"\n")
if tracker==len(cd):
    calc(rd,cd)
    print(np.array(cd),"\n")

for x in cd:
    for i in x:
        string=i
        if string != x[len(x)-1]:
            string = string +","
        out.write(string)

out.close()
