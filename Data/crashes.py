import pandas as pd
import psycopg2 as pg
import numpy as np
import sys, argparse, csv
import matplotlib as mt

def read_cell(x, y):
    with open('airplane_crashes.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

print (read_cell(4, 8))