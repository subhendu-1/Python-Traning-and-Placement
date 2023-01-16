
# this is 50 time fister then list
import numpy as np
import time
arr=np.array([1,2,4,5])
print(arr)
print(type(arr))


py_list=list(range(3000000)) #create of python list
arr=np.arange(3000000)  #Arrage functin is use to crate numpy array in range

begin=time.time()
new_lst=[i*2 for i in py_list]
end=time.time()
print("Time of exectuion for python list: ",end-begin)
begin=time.time()
new_arr=arr*2
end=time.time()
print("Time of exectuion for python list: ",end-begin)