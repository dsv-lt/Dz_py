import csv
import random
def Clear(y):
    z=""
    for i in range(len(y)):
        if y[i].isdigit() or y[i]=='.':
            z+=y[i]
    if z.count('.')==1 and z.rfind('.')!=len(z):
        return float(z)
    return float(z.replace('.',""))

A=[]
with open('data.csv','r',encoding='utf-8') as f:
    L=csv.reader(f)
    for row in L:
        A.append(list(map(Clear,row)))
#A=[list(map(Clear,l.split())) for l in f]
        
X,Y=[x[0] for x in A],[y[1] for y in A]
n=len(X)
S=[sum(X),sum(Y),sum(x**2 for x in X),sum(X[i]*Y[i] for i in range(n))]   
a=(S[0]*S[1]-n*S[3])/(S[0]**2-n*S[2])
b=(S[1]-a*S[0])/n

def MNK(xk,yk,a,b):
    return (yk-a*xk-b)**2

def F(X,Y,a,b):
    return sum(MNK(X[i],Y[i],a,b) for i in range(len(X)))

recReal=F(X,Y,a,b)
rec=[5000,0,0,1]
eps=float(input("Введите точность: "))
while max(abs(((rec[1]-a)**2+(rec[2]-b)**2)**0.5),abs(rec[0]-recReal))>eps:
    rec[3]+=1
    ar,br=random.uniform(-10,10),random.uniform(-10,10)
    recNew=F(X,Y,ar,br)
    if recNew<rec[0]:
        rec[0],rec[1],rec[2]=recNew,ar,br
    
print("Приближенное: ",round(rec[0],6),"| Реальное: ",recReal)
print("Приближенное a: ",round(rec[1],6),"| Реальное a: ",a)
print("Приближенное b: ",round(rec[2],6),"| Реальное b: ",b)
print("Колчество эпох: ",rec[3])