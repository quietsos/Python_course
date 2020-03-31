# Hash table and Hashmap is a type of data structure that maps keys to its value pairs

my_dic={'sohan':'001','sumon':'002',"sojib":"003"}
print(my_dic)
print(type(my_dic)) 

new_dic=dict()
print(new_dic)
print(type(new_dic))
new_dic=dict(sohan='001',sumon='002',sojib="003")
print(new_dic)

# Nested dictionary:
    #  Nested dictionary are basically dictionaries that lie within other dictionaries.

emp_details={'Employee':{'sohan':{'ID':'001','salary':'100','Designation':'Team leader'},
                        'sojib':{'ID':'002','salary':'200','Designation':'member'},
                        'sumon':{'ID':'003','salary':'300','Designation':'member'}}}
print(emp_details)

#Performaing Operations on Hash Table

print(my_dic['sohan'])
print(my_dic.keys())
print(my_dic.values())
print(my_dic.get("sojib"))


