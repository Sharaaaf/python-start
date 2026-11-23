import numpy as np 

# numpy for integer

array = np.array([1,2,3,4,0], dtype = np.int16) #int16 er jaygay float16 dilei data type changed
                                                #int16 er jaygay bool_ dile eta boolean hbe. 0 chara shb value true return korbe.
                                                #int16 er jaygay str_ dile eta string hbe. data type is <U1,<U2,<U3,<U4,<U5,<U6
# array = array * 2

array = array.astype(np.float16) #works for every data type conversion. just change np.anything

print(array.dtype)
print(f"{array.nbytes} bytes")
print(array)