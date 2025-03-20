from numpy import NAN
import pandas as pd


with open(r"C:\Users\MBSPL-Ayush\Desktop\topics.txt", 'r',encoding="utf-8") as file:
    # Read each line in the file
    for line in file:
        # Print each line
        if len(line) >1:
            print(line.strip())
            topics.append(line.strip())