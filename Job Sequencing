
class job:
    def __init__(self,deadline,time,profit,flag,index):
        self.deadline=deadline
        self.flag=flag
        self.time=time
        self.profit=profit
        self.index=index
list1=[]
list1.append(job(3,2,150,0,1))
list1.append(job(1,1,50,0,2))
list1.append(job(4,2,110,0,3))
list1.append(job(7,3,300,0,4))
list1.append(job(5,2,200,0,5))
list1.append(job(8,2,90,0,6))
list1.append(job(2,1,210,0,7))
list1.append(job(3,1,160,0,8))
list1.append(job(4,1,100,0,9))   
maxduration=0
global profit
profit=0
for item in list1:
    if(item.deadline>maxduration):
        maxduration=item.deadline
jobs=[]        
for i in range(0,maxduration):
    jobs.append(0)
    
    
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i].profit<list1[j].profit):
            t=list1[i]
            list1[i]=list1[j]
            list1[j]=t
            
            
#for item in list1:
 #   print("list1 asc {}".format(item.profit))
            
            
i=0  
while(i<len(list1) and list1[i].flag==0):
    #print("{} {}".format(i,list1[i].flag))
    
        f=0
        for j in range (0,list1[i].deadline):
            if(jobs[j]==0):
                f+=1
        #print(f"f is {f}")    
        if(f>=list1[i].time):
            
            count=0
            for j in range (list1[i].deadline-1,-1,-1):
                
                if(jobs[j]==0 and count<list1[i].time):
                    jobs[j]=list1[i].profit
                    count=count+1
            list1[i].flag=1
            profit+=list1[i].profit
            i=i+1
            
        else:
            i=i+1
    
    
    
        
        
#for item in jobs:
 #   print(item)  
#for item in list1:
 #   print("profit {},flag {},time {},deadline {} ,index{}".format(item.profit,item.flag,item.time,item.deadline,item.index))
    
    
for i in range (len(list1)):
    if(list1[i].flag==1):
        print(f"j{list1[i].index} is included")
    elif(list1[i].flag==0):
        print(f"j{list1[i].index} is not included")
    
print("profit is{}".format(profit))    
