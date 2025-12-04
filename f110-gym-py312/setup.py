# setup.py (Contents for ~/Desktop/F110_Gym_Setup/setup.py)
from setuptools import setup, find_packages

setup(
    name='f110_gym',  # The package name used for importing (matches the folder)
    version='1.0.1', 
    description='F1/10 Gym Environment updated for Python 3.12',
    author='NS',
    
    packages=find_packages(), # Finds the 'f110_gym' directory and its subpackages
    # Flags to correctly handle non-code data files
    include_package_data=True, 
    zip_safe=False,
)
