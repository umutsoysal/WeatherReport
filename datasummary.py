
import pandas as pd
import numpy as np

print("printing data")


import glob
files = glob.glob("*.txt")           # get all the .txt files

for file in files:                   # iterate over the list of files
    with open(file, "r") as fin:     # open the file
        # rest of the code