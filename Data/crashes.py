import pandas as pd
import psycopg2 as pg
import numpy as np
import sys, argparse, csv
import matplotlib as mt

def read_cell():
    with open('airplane_crashes.csv') as f:
        csv_reader = csv.reader(f)
    for line in csv_reader:
        l = line['Index']
        if l == index:
           crashes= print(line('location'))
    return(crashes)