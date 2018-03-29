## CONDENSATION ALGORITHM

from math import sqrt
import numpy as np


train= open ("3.txt","r")
##test=open ("4.txt","r")
cor=0
wor=0
ind=-1
trg=[]
trl=[]
##tsg=[]
##tsl=[]
htr=0
##hts=0
w=4
dist=[]

for line in train :
    x1,x2,x3,x4,x5=line.split(',')
    trg+=[[x1,x2,x3,x4]]
    trl+=[x5]
    htr+=1
##for line in test :
##    y1,y2,y3,y4,y5=line.split(',')
##    tsg+=([y1,y2,y3,y4])
##    tsl+=[y5]
##    hts+=1
trg=np.array(trg,dtype=np.float64)
##tsg=np.array(tsg,dtype=np.float64)
rd=[]
cd=[]
##for i in range(0,w):
##cd=[trg[0]]
##cd=np.array(cd,dtype=np.float64)
##rd=np.array(rd,dtype=np.float64)
##print(trg)
##print(cd)
##rd=trg-cd
##rd = [list(filter(lambda x: x in trg, sublist)) for sublist in cd]
##rd=[line for line in trg if line not in cd]
##a=0
##rd = np.delete(trg,0,0)
##print(rd)

##rd=np.where(trg not in cd)
##a=np.where(
print(rd)
a=[trg[0]]
d={0:a}
print(d)


##A = np.array([[1, 1, 1,], [1, 1, 2], [1, 1, 3], [1, 1, 4]])
##B = np.array([[0, 0, 0], [1, 0, 2], [1, 0, 3], [1, 0, 4], [1, 1, 0], [1, 1, 1], [1, 1, 4]])
##A_rows = trg.view([('', trg.dtype)] * trg.shape[1])
##B_rows = cd.view([('', cd.dtype)] * cd.shape[1])
##diff_array = np.setdiff1d(A_rows, B_rows).view(trg.dtype).reshape(-1, trg.shape[1])
##print (diff_array)
##rd=trg
####rd=np.all(trg == cd)
##rd=[x for x in trg if x not in cd]## + [x for x in cd if x not in trg])
####rd=filter(lambda x: x not in cd, trg)## + filter(lambda x: x not in trg,cd)
####rd=np.array(rd,dtype=np.float64)
##print(rd)
##ind=np.setdiff(trg,cd)
##print(trg)
##print(cd)
##print (ind)
##for i in cd:
##    for j in trg:
##        if np.all(i==j):
##            print(i)##rd=np.delete(trg,j,0)
##            rd=np.delete(rd,i,0)
##rd=np.array(rd,dtype=np.float64)
##print(rd)
##rd=np.delete(trg,cd,0)
##print(rd)
        

##for x in range(0,len(trg),w):
##    mindist=100
##    dist=[]
##    for y in range(0,len(cd),w):
##        print(trg[x],trg[x+1],trg[x+2],trg[x+3])
##        print(cd[y],cd[y+1],cd[y+2],cd[y+3])
##        dst=(((tsg[x]-trg[y])**2)+((tsg[x+1]-trg[y+1])**2)+((tsg[x+2]-trg[y+2])**2)+((tsg[x+3]-trg[y+3])**2))
##        dst=sqrt( dst)
##        dist+=[dst]
##        ##print(dst)
##        ##print()
##    print("********************")
##    for i in range(len(dist)):
##        if mindist>dist[i]:
##            mindist=dist[i]
##            ind=i
##    print("mindist=",mindist,"\nindex=",ind)
##    inde=int(x/4)
##    if tsl[inde]==trl[ind]:
##        print ("Correct")
##        print(inde,ind)
##        cor+=1
##    else:
##        print("Wrong")
##        print(inde,ind)
##        wor+=1
##    print ("--------------------")
##    print()
##    
##print()
##print("Number of training patterns =",htr)
##print("Number of test patterns =",hts)
##print("Correctly classified =",cor)
##print("Incorrectly classified =",wor)
##n=len(tsl)
##ca=(cor/n)*100
##print("Correct Accuracy=",ca)

