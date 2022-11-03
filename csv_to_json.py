from asyncore import write
import csv
import json
import pandas as pd
from os import write
import codecs

ifile =  open("NFT_Naming_csv.csv", "rb")
reader = csv.reader(codecs.iterdecode(ifile, 'utf-8'))
    
data = []
    
for row in reader:
    print(row)
