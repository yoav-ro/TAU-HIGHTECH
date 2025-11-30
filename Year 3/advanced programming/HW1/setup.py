from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("exercise_solution.py")
)