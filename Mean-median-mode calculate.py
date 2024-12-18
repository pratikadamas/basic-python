
import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)


q=int(input("---------- Enter your data values:--------\n No of data item present ",))
list=[]  # empty list
for i in range(q):
     data=int(input())    # list initialized by append() or insert() function
   # list.append(data)
     list.insert(i,data)



a,b,c= result =mean_median_mode(list)

print(f"The mean value {a} , median value {b} , mode value {c}")

print(result)