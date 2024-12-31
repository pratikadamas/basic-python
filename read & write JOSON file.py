
import json
file=open(r"E:\basic python\json file.py","r")
data =file.read()

final_data=json.loads(data)

# print(final_data)


for a in final_data:

    print(a," : ",final_data[a])