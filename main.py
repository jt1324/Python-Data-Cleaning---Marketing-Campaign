import pandas as pd
import numpy as np

# Load messy data
df = pd.read_csv('marketing_campaign_data_messy.csv')

print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")

