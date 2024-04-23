import pandas as pd

# Read the CSV file
csv_file = "Extracted/extracted_a.csv"
df = pd.read_csv(csv_file)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Add new empty column "Grade"
df['Grade'] = ''

# Write the cleaned data to a new CSV file
cleaned_csv = "Cleaned/cleaned_a.csv"
df.to_csv(cleaned_csv, index=False)
