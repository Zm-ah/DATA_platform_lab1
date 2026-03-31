import pandas as pd 
import os 

# extract läser data från csv file
df = pd.read_csv('data/products.csv', sep=';')
print ("====== Data Extracted from CSV File ====")
print (df.head())
print ("\nKolonner: ", df.columns.tolist())


# transform - städning av data 


df['name'] = df['name'].astype(str).str.strip()
df['currency']= df['currency'].astype(str).str.strip()
df['price']= pd.to_numeric(df['price'],errors='coerce')

print ("\n====== Data Transformed ====")
print (df.head())


# flag -  möjliga problem med data

# Saknar currency
df['flag_missing_currency'] = df['currency'].isna()

# Negativt pris
df['flag_negative_price'] = df['price'] < 0

# Extremt högt pris (t.ex. över 1000)
df['flag_high_price'] = df['price']> 10000

# Pris = 0
df['flag_zero_price'] = df['price'] == 0
# Null-ID, id som saknas eller är NaN
df['flag_missing_id'] = df['id'].isna()

print("\n==== >Falaggade produkter< ====")
print("Saknar cyrrency:",df['flag_missing_currency'].sum())
print("Negativt pris:", df['flag_negative_price'].sum())
print("Extrem hög pris:", df['flag_high_price'].sum())
print("Noll pris:", df['flag_zero_price'].sum())

print("\nDEBUG:")
print(df[['id','price','currency',
          'flag_missing_currency',
          'flag_negative_price',
          'flag_high_price',
          'flag_zero_price']])



# REJECT - ta bort rader som har flaggor

df_clean = df[
    (df['flag_missing_currency'] == False) &
    (df['flag_negative_price'] == False) &
    (df['flag_zero_price'] == False)&
    (df['flag_missing_id'] == False)
]

print("\n====== Clean Data (Efter Reject) ======")
print(df_clean.head())
print("\nAntal rader före:", len(df))
print("Antal rader efter:", len(df_clean))



# load data till analytics_summary.csv

analytics_summary = pd.DataFrame({
    'snittpris': [df_clean['price'].mean()],
    'medianpris': [df_clean['price'].median()],
    'antal_produkter': [len(df_clean)],
    'antal_produkter_med_saknat_pris': [df['price'].isna().sum()]
})

analytics_summary.to_csv('analytics_summary.csv', index=False)
print("\nAnalytics summary saved to analytics_summary.csv")
