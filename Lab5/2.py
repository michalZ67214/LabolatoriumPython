sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

# for k, v in sample_dict.items():
#     print(k,v)

for k in sample_dict.keys():
 print(f'{k:<10} = {sample_dict[k]:>10}')