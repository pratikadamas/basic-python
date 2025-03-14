import pandas as pd

# Data Frame

# l=[1,2,3,4]
# var=pd.DataFrame(l,index=['A','B','C','D'])
# # print(var.head())
# print(var)
#
# l1={"a":[1,2,3,4,5,6,7,8,9],"b":[1,2,3,4,5,6,7,8,9],"c":[1,2,3,4,5,6,7,8,9]}
# # l2=pd.DataFrame(l1,columns=["a","b","c"])
# print(l2["a"])
# l2["a"][2]=126
# print("value at index",l2["a"][2])
# print(l2)

# list_1 = [[12,23,4,5],[12,23,4,5],[123,126,58,9]]
# data=pd.DataFrame(list_1)
# print(data)
# x=pd.DataFrame({"a":[1,2,3,4],"b":[1,2,3,4]})
# x["c"]= x["a"]+x["b"]
# print(x)


# # MODIFING DATAFRAME
#
# gf = {'A': [1, 2, 3],'B': [4, 5, 6],'C': [7, 8, 9]}
# df = pd.DataFrame(gf, columns=['A', 'B', 'C'])
# print(df)
# df['D'] = df['A'] + df['B']
# print(df)
# df=df.rename(columns={'A':"AA",'B':"BB"})
# df = df.drop(columns=["C"])
# print(df)
#
# # result = df.drop(0)
#
#
# result = df[df["AA"]>2]
# print(result)



