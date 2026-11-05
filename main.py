import pandas as pd
import numpy as np


# Load messy data
df = pd.read_csv('marketing_campaign_data_messy.csv')

print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")


# Checking the data
pd.set_option("display.max_columns", None)  # show every column
pd.set_option("display.width", None)        # use the full terminal width
pd.set_option("display.max_colwidth", 40)   # keep long text from being cut off
pd.set_option("display.max_rows", 20)       # show 20 rows, not all 2,020

print(df.head(20).to_string())


# Header cleaning
print(df.columns.tolist())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("Headers fix applied!")
print(df.columns.tolist())


# Type conversion & currency cleaning
dirty_spend_mask = df['spend'].astype(str).str.contains(r'\$')
print(df.loc[dirty_spend_mask, ['campaign_id', 'spend']].head(3))

df['spend'] = df['spend'].astype(str).str.replace(fr'[^\d.-]', '', regex=True)
df['spend'] = pd.to_numeric(df['spend'])

print("Values fix applied!")
print(df.loc[dirty_spend_mask, ['campaign_id', 'spend']].head(3))


# Categorical typos (Fuzzy logic)
print(df['channel'].unique())



