import json

f=open('text.json')
data=f.read()
print(type(data))
data_dict=json.loads(data)
print(type(data_dict))
print(data_dict['loc'])
# print(len(data_dict['subs']))