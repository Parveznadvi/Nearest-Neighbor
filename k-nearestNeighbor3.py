## K-NEAREST-NEIGHBOR ALGORITHM

from math import sqrt

train= open ("train.txt","r")
test=open ("test.txt","r")
cor=0
wor=0
ind=-1
trg=[]
tsg=[]
a=[]
k=int(input("Enter the value of k:"))

for line in train :
    trg+=[line.split(',')]
for line in test :
    tsg+=[line.split(',')]
w=len(trg[0])-1

while k >len(trg) :
    print("k value should be less than",len(trg)+1,"please enter again")
    k=int(input("Enter the value of k:"))
    
for i in range(len(trg)):
    a+=[i]

def kmin(dist):
    global k
    lb=[]
    rst=[]
    prs=dict(zip(a,dist))
    prs=sorted(prs,key=prs.get)
    for i in range(0,k):
        rst+=[prs[i]]
    for i in range(len(rst)):
        lb+=[trg[rst[i]][w]]
    kn=occur(lb)
    kn=list(kn)
    return (kn[0])   

def occur(items):
    d = {}
    for i in items:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d
 
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
    kn=kmin(dist)   
    inde=int(x)
    t=tsg[inde][w]
    if t==kn:
        print ("Correct")
        print(t,kn)
        cor+=1
    else:
        print("Wrong")
        print(t,kn)
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
