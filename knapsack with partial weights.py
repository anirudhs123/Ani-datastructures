
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
        if((list1[i].profit/list1[i].weight)<(list1[j].profit/list1[j].weight)):
            t=list1[i]
            list1[i]=list1[j]
            list1[j]=t

profit=0            
while(m>0):
    for i in range(n):
        if(m>=list1[i].weight):
            profit+=list1[i].profit
            m=m-list1[i].weight
        elif(m>0 and m<list1[i].weight):
            profit+=(list1[i].profit)*(m/list1[i].weight)
            m=0
            break
            
print(f"profit is {profit}")            
            
            
