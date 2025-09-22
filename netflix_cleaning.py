import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Handle missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")

df.dropna(subset=['title'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text
df['type'] = df['type'].str.lower().str.strip()

# Fix date format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Ensure correct datatypes
df['release_year'] = df['release_year'].astype(int)

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
print("✅ Cleaned dataset saved as netflix_cleaned.csv")
