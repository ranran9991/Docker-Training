import pandas as pd
import os

# Define the data directory (to be mounted as a volume)
DATA_DIR = "/app/data"
CSV_FILE = os.path.join(DATA_DIR, "user_data.csv")

# Initialize CSV if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["user_id", "name", "score"])
        df.to_csv(CSV_FILE, index=False)

# Add a new entry to the CSV
def add_entry(user_id, name, score):
    initialize_csv()
    df = pd.read_csv(CSV_FILE)
    new_entry = pd.DataFrame({"user_id": [user_id], "name": [name], "score": [score]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    return df

# Read and display the CSV
def read_csv():
    initialize_csv()
    df = pd.read_csv(CSV_FILE)
    return df.to_string()

if __name__ == "__main__":
    # Example: Add a new entry and display the CSV
    add_entry(1, "Alice", 95)
    print("Current CSV content:")
    print(read_csv())