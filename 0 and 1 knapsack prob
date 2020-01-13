
class sack:
    def __init__(self,weight,profit,flag):
        self.profit=profit
        self.weight=weight
        self.flag=flag
        
list1=[]

list1.append(sack(2,1,0))
list1.append(sack(3,2,0))
list1.append(sack(4,5,0))
list1.append(sack(5,6,0))

m=int(input("please enter max weight   "))
n=len(list1)      
for i in range(n):
      for j in range(i+1,n):
        if(list1[i].weight>list1[j].weight):
            t=list1[i]
            list1[i]=list1[j]
            list1[j]=t
    
import numpy as np
k=np.ones((n+1,m+1))     
      
    
for i in range(0,n+1):
    for w in range(0,m+1):
        if(i==0 or w==0):
            k[i][w]=0
        elif(list1[i-1].weight<=w ):
            if(list1[i-1].profit+k[i-1][w-list1[i-1].weight]>k[i-1][w]):
                k[i][w]=list1[i-1].profit+k[i-1][w-list1[i-1].weight]
                
            else:
                k[i][w]=k[i-1][w]
        else: 
            k[i][w]=k[i-1][w]
            
            
print(f"max profit is {k[n][w]}")            
k            
