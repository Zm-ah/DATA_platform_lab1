import pandas as pd 
import os 

# extract data from csv file
df = pd.read_csv('data/products.csv', sep=';')
print ("====== Data Extracted from CSV File ====")
print (df.head())
print ("\nKolumter: ", df.columns.tolist())

