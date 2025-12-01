import numpy as np
import cython
import time
import random

# Part 1

# Pure Python
def func_pure_python(x_list):
    res_list =[]
    for num in x_list:
        res_list.append(3* (num**2) - 2*num +5)
    return res_list

# NumPy vectors
def func_np_vec(x_list):
    vec = np.array(x_list)
    transform= 3 * (vec**2) - 2 * vec + 5
    return transform.tolist()

# Cython loop
def func_cython(x_list: cython.int[:]):
    lst_legnth: cython.int = len(x_list)
    i: cython.int
    val: cython.int
    
    res_list = [0] * lst_legnth

    for i in range(lst_legnth):
        val = x_list[i]
        res_list[i] = 3 * (val**2) - 2 * val + 5
        
    return res_list

# Cython vectors
def func_cython_vec(x_list: cython.int[:]):
    vec: cython.int[:] = np.array(x_list)

    lst_legnth: cython.int = vec.shape[0]
    i: cython.int
    val: cython.int
    
    # Create a NumPy array for the result (allocated in C via NumPy)
    # dtype must match the cython type (cython.int -> np.int32)
    res_np = np.zeros(lst_legnth, dtype=np.int32)
    
    # Create a typed memoryview on the result array to allow fast C-access during write
    # This is critical: writing to res_np[i] directly is slower (Python call)
    # Writing to res_view[i] is fast (C pointer arithmetic)
    res_view: cython.int[:] = res_np

    # Loop over C index
    for i in range(lst_legnth):
        val = vec[i]
        # Write directly to the memory address of the numpy array
        res_view[i] = 3 * (val**2) - 2 * val + 5
        
    return res_np

def generate_list(n, lower, upper):
    if n < 0:
        raise ValueError("n (number of elements) must be non-negative.")
    if lower > upper:
        raise ValueError("Lower bound cannot be greater than upper bound.")

    return [random.randint(int(lower), int(upper)) for _ in range(n)]

def print_run_time(func, list, func_desc):
    start= time.time()
    func(list)
    end=time.time()
    print("Function %s took %s to run." %(func_desc, round(end-start,5)))

def run_q1():
    list10k=generate_list(10000, 0,10)
    list100k=generate_list(100000, 0,10)
    list1m=generate_list(1000000, 0,10)
    list5m=generate_list(5000000, 0,10)

    # Test 10k list
    print("Testing a 10k items list:")
    print_run_time(func_pure_python, list10k, "Pure python loop")
    print_run_time(func_np_vec, list10k, "Numpy vectors")
    print_run_time(func_cython, list10k, "Normal Cython")
    print_run_time(func_cython_vec, list10k, "Cython vectors")

    # Test 100k list
    print("Testing a 100 k items list:")
    print_run_time(func_pure_python, list100k, "Pure python loop")
    print_run_time(func_np_vec, list100k, "Numpy vectors")
    print_run_time(func_cython, list100k, "Normal Cython")
    print_run_time(func_cython_vec, list100k, "Cython vectors")

    # Test 1m list
    print("Testing a 1m items list:")
    print_run_time(func_pure_python, list1m, "Pure python loop")
    print_run_time(func_np_vec, list1m, "Numpy vectors")
    print_run_time(func_cython, list1m, "Normal Cython")
    print_run_time(func_cython_vec, list1m, "Cython vectors")

    # Test 5m list
    print("Testing a 5m items list:")
    print_run_time(func_pure_python, list5m, "Pure python loop")
    print_run_time(func_np_vec, list5m, "Numpy vectors")
    print_run_time(func_cython, list5m, "Normal Cython")
    print_run_time(func_cython_vec, list5m, "Cython vectors")

run_q1()