list=[1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
dic={}
for i in list:
    if i in dic:
        dic[i]+=1
    else:
         dic[i]=1


print(dic)
