#Converting a dictionary into a dataframe:
    # DataFrame is a 2-D(2-dimentional) data structure that consist of colums of various types. It is very similar to python dictionary and you can even convert a dictionaty inot a pandas dataframe 


emp_details={'Employee':{'sohan':{'ID':'001','salary':'100','Designation':'Team leader'},'sojib':{'ID':'002','salary':'200','Designation':'member'},'sumon':{'ID':'003','salary':'300','Designation':'member'}}}
print(emp_details)



import pandas as pd 
df = pd.DataFrame(emp_details['Employee'])
print(df) 