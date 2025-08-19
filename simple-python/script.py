import pandas as pd

# Sample script to load and summarize a CSV
data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 75000]
})
# Save to CSV for demo
data.to_csv('data.csv', index=False)
# Read and summarize
df = pd.read_csv('data.csv')
print("Dataset Summary:")
print(df.describe())