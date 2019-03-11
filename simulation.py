import numpy as npy
import matplotlib.pyplot as plt
import math

def Average(lst): 
    return sum(lst) / len(lst)

siz = 100000
printsz = 10
x,c1,c2,p = [],[],[],[]
c1elements = [43,44,45,46,47]
c1prob = [0.1,0.2,0.4,0.2,0.1]
mux,sigmax = 15000, 4500
loss = 0

for i in range(siz): 
    x.append(npy.random.normal(mux,sigmax))
    c1.append(npy.random.choice(c1elements, p=c1prob))
    c2.append(npy.random.uniform(80.0,100.0))
    
    prof = (249 - c1[i] - c2[i])*x[i] - 1000000
    p.append(prof)
    
    if (prof<0):
        loss+=1


print('\t  profit\t  demand     direct lc       parts costs\n')
for i in range (printsz):
    print(i+1,'\t','%.2f'%p[i] , '\t' , '%.2f'%x[i] , '\t' , c1[i] , '\t\t' , '%.2f'%c2[i] , '\n') 

print('Maximum Profit = ',max(p),'\n')
print('Minimum Profit = ',min(p),'\n')
print('Average Direct labor cost = ',Average(c1),'\n')
print('Average Parts cost = ',Average(c2),'\n')
print('Average profit = ',Average(p),'\n')
print('Average demand = ',Average(x),'\n')
print('Total Direct labor cost = ',sum(c1),'\n')
print('Total Parts cost = ',sum(c2),'\n')
print('Total profit = ',sum(p),'\n')
print('Total demand = ',sum(x),'\n')
print('Probability of loss = ',loss/len(p),'\n')

n = 500

plt.title('Demand histogram')
plt.hist(x,n, color='red')
plt.show()

plt.title('Profit histogram')
plt.hist(p,n, color='blue')
plt.show()

plt.title('Total Direct labor cost histogram')
plt.hist(c1,5, color='green')
plt.show()

plt.title('Total parts cost')
plt.hist(c2,20, color='black')
plt.show()
