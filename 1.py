from math import sqrt

train= open ("3.txt","r")
out=open("new.txt","w+")
trg=[]
string=""

for line in train :
    trg+=[line.split(',')]
#print(trg)

for x in trg:
    for i in x:#range(0,len(x)):
        string=i#x[i]#,x[1],x[2],x[3],x[4]
        #string=str(string)
        if string != x[len(x)-1]:
            string = string +","
    #if string.startswith('"') and string.endswith('"'):
        #string = string[1:-1]
        #print(string)
        #print()
        #print(string.replace('(', '').replace(')', '').replace('\'', ''))
        out.write(string)#.replace('[', '').replace(']', '').replace('\'','').replace('\\n','').lstrip())
        #out.write(',')
    #out.write('\n')

#if string.startswith('"') and string.endswith('"'):
#    string = string[1:-1]

out=open("new.txt","r")
for line in out:
    print(line)

##str1=" IRIS\n"
##str2="IRIS\n"
##if str1==str2:
##    print("true")
##else:
##    print("false")



##x=[]
##y=[]
##cor=0
##md=100
##
##for line in test :
##    y=float(line.split(','))
##    for line in train :
##        x=float(line.split(','))
##    dist =  sqrt( (x[1]-x[2])**2)
####        dist=sqrt((x[1]-y[1])**2 + (x[2]-y[2])**2 + (x[3]-y[3])**2  + (x[4]-y[4])**2 )
##    print(dist)
##train.close()
##test.close()
##import numpy as np
##A = np.array([[1, 1, 1,], [1, 1, 2], [1, 1, 3], [1, 1, 4]])
##B = np.array([[0, 0, 0], [1, 0, 2], [1, 0, 3], [1, 0, 4], [1, 1, 0], [1, 1, 1], [1, 1, 4]])
##A_rows = A.view([('', A.dtype)] * A.shape[1])
##B_rows = B.view([('', B.dtype)] * B.shape[1])
##diff_array = np.setdiff1d(A_rows, B_rows).view(A.dtype).reshape(-1, A.shape[1])
##print(A)
##print(B)
##print(A_rows)
##print(B_rows)
##print(diff_array)

##from sklearn.datasets import load_iris
##from sklearn import cross_validation
##import numpy as np
##
### load dataset and partition in training and testing sets
##iris = load_iris()
##X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=1)
##
### reformat train/test datasets for convenience
##train = np.array(zip(X_train,y_train))
##test = np.array(zip(X_test, y_test))
####print(train)
####print(test)
##
##
### 1) given two data points, calculate the euclidean distance between them
##def get_distance(data1, data2):
##    points = zip(data1, data2)
##    diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
##    return math.sqrt(sum(diffs_squared_distance))
