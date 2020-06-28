details =[{'name':'Ram','age':20},{'name':'Nick','age':19},{'name':'Maddy','age':21},{'name':'Adamm','age':33}]
print("Original list of Dictionaries : ", details)
sorted_age = sorted(details,key=lambda x: x['age'],reverse=False)
print("\nSorted list of Dictionaries according to age: ",sorted_age)

print('\n')
sorted_names = sorted(details,key=lambda x: x['name'])
print("Sorted list of Dictionaries according to name: ",sorted_names)
