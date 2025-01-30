import csv

# Data with inconsistent rows
data = [
    ["Name", "Age", "Country"],         # Header row
    ["Alice", 30, "USA"],              # Valid row
    ["Bob", 25],                       # Missing one column
    ["Charlie", 35, "UK", "Extra"],    # Extra column
]

# Step 1: Normalize rows
max_columns = max(len(row) for row in data)  # Find the maximum number of columns

normalized_data = []
for row in data:
    if len(row) < max_columns:
        # Fill missing columns with empty strings
        row.extend([""] * (max_columns - len(row)))
    elif len(row) > max_columns:
        # Trim extra columns
        row = row[:max_columns]
    normalized_data.append(row)

# Step 2: Write to CSV
output_file = "output.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(normalized_data)

print(f"CSV file '{output_file}' created successfully!")
