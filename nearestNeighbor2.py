## NEAREST-NEIGHBOR ALGORITHM

from math import sqrt

train= open ("cnddd.txt","r")
test=open ("test.txt","r")
cor=0
wor=0
ind=-1
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
    for y in range(0,len(trg)):
        dst=0
        ##print(tsg[x][0],tsg[x][1],tsg[x][2],tsg[x][3])
        ##print(trg[y][0],trg[y][1],trg[y][2],trg[y][3])
        for i in range(0,w):
            dst+=((float(tsg[x][i])-float(trg[y][i]))**2)
        dst=sqrt( dst)
        dist+=[dst]
        ##print(dst)
        ##print()
    print("********************")
    for i in range(len(dist)):
        if mindist>dist[i]:
            mindist=dist[i]
            ind=i
    ##print("mindist=",mindist,"\nindex=",ind)
    inde=int(x)
    if tsg[inde][w]==trg[ind][w]:
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
print("Number of training patterns =",len(trg))
print("Number of test patterns =",len(tsg))
print("Correctly classified =",cor)
print("Incorrectly classified =",wor)
ca=(cor/len(tsg))*100
print("Correct Accuracy=",ca)
