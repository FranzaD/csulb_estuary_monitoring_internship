import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel data
df = pd.read_excel('fishseines.xlsx')

# 1. Quick overview of dataset structure & missing values
print("--- DATA INFO ---")
print(df.info())

# 2. Numerical summary (mean, std, min, max, quartiles)
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())

# 3. Categorical counts (e.g., sample counts per site)
# Replace 'site' with an actual column name from your spreadsheet
if 'site' in df.columns:
    print("\n--- SAMPLES PER SITE ---")
    print(df['site'].value_counts())

# 4. Grouped summary (e.g., mean invertebrate count per site)
# Replace 'abundance' and 'site' with your real column names
# grouped_summary = df.groupby('site')['abundance'].agg(['mean', 'median', 'std'])
# print(grouped_summary)
