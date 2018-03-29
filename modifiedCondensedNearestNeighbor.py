## MODIFIED CONDENSED NEAREST-NEIGHBOR ALGORITHM
import numpy as np
from math import sqrt

train = open ("train.txt","r")
out=open("pro.txt","w")
trg=[]
pro=[]
typ=[]
sub=[]
lb=[]
subb=[]

for line in train :
    trg+=[line.split(',')]
w=(len(trg[0])-1)

lb=[trg[0][w]]
for l in trg:
    if l[w] not in lb:
        lb+=[l[w]]

def centroid(lb,trg):
    typ=[]
    for x in lb:
        c=0
        one=0.0
        two=0.0
        three=0.0
        four=0.0
        dif=0.0
        for y in trg:
            if x==y[w]:
                c+=1
                one+=float(y[0])
                two+=float(y[1])
                three+=float(y[2])
                four+=float(y[3])
        if one and two and three and four!=0:
            typ+=[[one/c,two/c,three/c,four/c,x]]
    return typ
typ=centroid(lb,trg)
pro=pro+typ

def classify(trg,pro,sub):
    cor=0
    wor=0
    ind=-1
    sub=[]
    for x in range(0,len(trg)):
        mindist=100
        dist=[]
        for y in range(0,len(pro)):
            ##print(trg[x][0],trg[x][1],trg[x][2],trg[x][3])
            ##print(pro[y][0],pro[y][1],pro[y][2],pro[y][3])
            dst=((float(trg[x][0])-float(pro[y][0]))**2)\
                 +((float(trg[x][1])-float(pro[y][1]))**2)\
                 +((float(trg[x][2])-float(pro[y][2]))**2)\
                 +((float(trg[x][3])-float(pro[y][3]))**2)
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
        if trg[inde][w]==pro[ind][w]:
            #print ("Correct")
            #print(inde,ind)
            cor+=1
        else:
            #print("Wrong")
            #print(inde,ind)
            wor+=1
            sub+=[trg[inde]]
        #print ("--------------------")
        #print()
    print()
    print("Number of training patterns =",len(pro))
    print("Number of test patterns =",len(trg))
    print("Correctly classified =",cor)
    print("Incorrectly classified =",wor)
    n=len(trg)
    ca=(cor/n)*100
    print("Correct Accuracy=",ca)
    print()
    print ("--------------------")
    return sub       
sub=classify(trg,pro,sub)

##print(lb)
##print()
##print(np.array(trg))
##print()
##print(np.array(typ))
##print()
##print(np.array(pro))
##print()
##print(np.array(sub))
##print()

def reclass(sub):
    global pro
    if sub!=[]:
        typ=centroid(lb,sub)
        print(np.array(typ))
        sub=classify(sub,typ,subb)
        print(np.array(sub))
    pro=pro+typ     

while sub!=[]:
    reclass(sub)
    sub=classify(trg,pro,subb)
    print()
    print(np.array(sub))
    print()
    print(np.array(pro))

for x in pro:
    for i in x:
        string=i
        string=str(string)
        if string != x[len(x)-1]:
            string = string +","
        out.write(string)
out.close()
