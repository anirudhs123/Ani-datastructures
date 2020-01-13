

dict={"a":0,"b":0,"c":0,"d":0,"e":0}

msg='bccabbddaeccbbaeddccaabbbcccddeeabse'
for i in msg:
    if(i=='a'):
        dict['a']+=1
    if(i=='b'):
        dict['b']+=1
    if(i=='c'):
        dict['c']+=1
    if(i=='d'):
        dict['d']+=1
    if(i=='e'):
        dict['e']+=1
print("number of a are {}".format(dict['a']))    
print("number of b are {}".format(dict['b']))    
print("number of c are {}".format(dict['c']))    
print("number of d are {}".format(dict['d']))    
print("number of e are {}".format(dict['e']))    


class letter:
    
    def __init__(self,count,alph,flag):
        
        self.count=count
        self.flag=flag
        self.alph=alph
        self.code=''

list1=[]   
list1.append(letter(dict["a"],"a",0))
list1.append(letter(dict['b'],"b",0))
list1.append(letter(dict["c"],"c",0))
list1.append(letter(dict["d"],"d",0))
list1.append(letter(dict["e"],"e",0))

n=5
m=5
for i in range(0,5):
    for j in range(i+1,5):
        if(list1[i].count>list1[j].count):
            t=list1[i]
            list1[i]=list1[j]
            list1[j]=t
list2=[]
k=0
while(n>1 and k<m):
    #print("k is {}".format(k))
    if(list1[k].flag==0):
        list1.append(letter(list1[k].count+list1[k+1].count,list1[k].alph+list1[k+1].alph,0))
        list1[k].flag=1
        list2.append(list1[k].count)
        list1[k+1].flag=1
        list2.append(list1[k+1].count)
        n=n-1
        m=m+1
       # print("n is {}".format(n))
        #print("m is {}".format(m))
        for i in range(0,m):
            for j in range(i+1,m):
                if(list1[i].count>list1[j].count and list1[i].flag==0 and list1[j].flag==0):
                    t=list1[i]
                    list1[i]=list1[j]
                    list1[j]=t 
    else:
        k=k+1
              
                         
for item in list1:
    print(" list1 {}".format(item.count))

l=0  
a=[]

while(l<m):
    #print(f"{m}")
    
    a.append(letter(list1[l].count,list1[l].alph,0))
    pos=l
   
    while(pos>0 and (a[pos].count>a[pos//2].count or a[pos].count>a[pos//2-1].count)) :
        if(pos%2==0):
            t=a[pos]
            a[pos]=a[pos//2-1]
            a[pos//2-1]=t
            pos=pos//2-1
        else:
            t=a[pos]
            a[pos]=a[pos//2]
            a[pos//2]=t
            pos=pos//2
            
    l=l+1    

    
    
    
for i in range(0,len(a)):
    if(a[i].alph=="a" or a[i].alph=="b" or a[i].alph=='c' or a[i].alph=="d" or a[i].alph=="e"):
        if(i==1):
            a[i].code+='0'
        elif(i==2):
            a[i].code+='1'
        elif(i==3):
            a[i].code+='00'
        elif(i==4):
            a[i].code+='01'
        elif(i==5):
            a[i].code+='10'
        elif(i==6):
            a[i].code+='11'
        elif(i==7):
            a[i].code+='000'
        elif(i==8):
            a[i].code+='001'
        
        
for item in a:       
    print("  {} {} {}".format(item.count,item.alph,item.code))
    
