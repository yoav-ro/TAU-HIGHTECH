import numpy as np
import cython
import time
import random
import pandas as pd
import csv
import re

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
    transform: cython.int[:] = 3 * (vec**2) - 2 * vec + 5
    return transform.tolist()

def generate_list(n, lower, upper):
    if n < 0:
        raise ValueError("n (number of elements) must be non-negative.")
    if lower > upper:
        raise ValueError("Lower bound cannot be greater than upper bound.")

    return [random.randint(int(lower), int(upper)) for _ in range(n)]

def print_run_time(func, args, func_desc):
    start= time.time()
    func(*args)
    end=time.time()
    print("Function %s took %s to run." %(func_desc, round(end-start,5)))

def run_q1():
    list10k=generate_list(10000, 0,10)
    list100k=generate_list(100000, 0,10)
    list1m=generate_list(1000000, 0,10)
    list5m=generate_list(5000000, 0,10)

    # Test 10k list
    print("Testing a 10k items list:")
    print_run_time(func_pure_python, [list10k], "Pure python loop")
    print_run_time(func_np_vec, [list10k], "Numpy vectors")
    print_run_time(func_cython, [list10k], "Normal Cython")
    print_run_time(func_cython_vec, [list10k], "Cython vectors")

    # Test 100k list
    print("Testing a 100 k items list:")
    print_run_time(func_pure_python, [list100k], "Pure python loop")
    print_run_time(func_np_vec, [list100k], "Numpy vectors")
    print_run_time(func_cython, [list100k], "Normal Cython")
    print_run_time(func_cython_vec, [list100k], "Cython vectors")

    # Test 1m list
    print("Testing a 1m items list:")
    print_run_time(func_pure_python, [list1m], "Pure python loop")
    print_run_time(func_np_vec, [list1m], "Numpy vectors")
    print_run_time(func_cython, [list1m], "Normal Cython")
    print_run_time(func_cython_vec, [list1m], "Cython vectors")

    # Test 5m list
    print("Testing a 5m items list:")
    print_run_time(func_pure_python, [list5m], "Pure python loop")
    print_run_time(func_np_vec, [list5m], "Numpy vectors")
    print_run_time(func_cython, [list5m], "Normal Cython")
    print_run_time(func_cython_vec, [list5m], "Cython vectors")

# Part 2

# Extract the fist word from each description
# Using python loop with the re module
def extract_first_word_using_re(csv_path):
    first_word_list=[]
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            desc= row["description"]
            match = re.search(r"^\s*(\w+)", desc)
            if match:
                first_word_list.append(match.group(1))
            else:
                first_word_list.append("")

    return first_word_list

# Using pandas.str.extract with regex
def extract_first_word_using_pandas_regex(csv_path):
    df=pd.read_csv(csv_path)
    return df["description"].str.extract(r"^(\w+)")

def get_customer_total_python_loop(csv_path):
    totals_dict={}
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer= row["customer_id"]
            amount=float(row["amount"])
            if customer in totals_dict:
                totals_dict[customer] += amount
            else:
                totals_dict[customer] = 0.0

    return totals_dict

def get_customer_total_pandas_groupby(csv_path):
    df=pd.read_csv(csv_path)
    return df.groupby("customer_id")["amount"].sum()

def get_customer_total_pandas_vectors(csv_path):
    df=pd.read_csv(csv_path)
    return df.pivot_table(index="customer_id", values="amount", aggfunc="sum")["amount"].to_dict()


def run_q2():
    path="transactions.csv"
    print("Extracting the first word of the description")
    print_run_time(extract_first_word_using_re, [path], "extract first word using re")
    print_run_time(extract_first_word_using_pandas_regex, [path], "extract first word using pandas and regex")
    print("Getting the sum of amount spend by customer")
    print_run_time(get_customer_total_python_loop, [path], "get sums using a python loop")
    print_run_time(get_customer_total_pandas_groupby, [path], "get sums using pandas and groupby")
    print_run_time(get_customer_total_pandas_vectors, [path], "get sums using pandas vectorized")


def run_hw():
    print("Q1:")
    run_q1()
    print("Q2:")
    run_q2()

run_hw()