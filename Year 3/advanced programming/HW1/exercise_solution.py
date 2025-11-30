import numpy as np
import cython

# Part 1

# Pure Python
def func_pure_python(x_list):
    res_list =[]
    for num in x_list:
        res_list.append(3* (num**2) - 2*num +5)
    return res_list

# NumPy vectors
def func_np_vec(x_vec):
    return 3 * x_vec**2 - 2 * x_vec + 5

# Cython loop
def func_cython(x_arr: cython.int[:]):
    arr_length: cython.int = x_arr.shape[0]
    i: cython.int
    val: cython.int
    
    res_list = [0] * arr_length

    for i in range(arr_length):
        val = x_arr[i]
        res_list[i] = 3 * (val**2) - 2 * val + 5
        
    return res_list

# Cython vectors
def func_cython_vec(x_array: cython.int[:]):
    """
    Uses a NumPy array for the output buffer as well.
    We create a view on the output array to fill it at C-speed.
    """
    # Get length as C integer
    n: cython.int = x_array.shape[0]
    i: cython.int
    val: cython.int
    
    # Create a NumPy array for the result (allocated in C via NumPy)
    # dtype must match the cython type (cython.int -> np.int32)
    res_np = np.zeros(n, dtype=np.int32)
    
    # Create a typed memoryview on the result array to allow fast C-access during write
    # This is critical: writing to res_np[i] directly is slower (Python call)
    # Writing to res_view[i] is fast (C pointer arithmetic)
    res_view: cython.int[:] = res_np

    # Loop over C index
    for i in range(n):
        val = x_array[i]
        # Write directly to the memory address of the numpy array
        res_view[i] = 3 * (val**2) - 2 * val + 5
        
    return res_np

print(func_pure_python(3))