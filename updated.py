import re
import pandas as pd

# Define column names exactly as specified
columns = [
    "LAB", "DATE", "STATION", "OFFSET", "ELOV", 
    "MECHANICAL ANALYSIS % FINER 1 1/2", "3/4", "4", "200", "5U",
    "ATT LIMITS L.L", "P.I", "SPEC GRAV +", "-", 
    "FEILD DENSITY DRY", "%", "DRY", "MOIST", 
    "METHOD A MAX DRY", "METHOD A OPT", 
    "METHOD MAX DRY", "OPT", "METHOD_ MAX DRY", "OPT", "COMPACTION"
]

# Load the OCR-extracted text file
with open(r"C:\Users\anany\Desktop\LLM-OCR\output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Function to extract only numerical data from each line
def extract_numbers(line):
    return re.findall(r"\d+\.?\d*", line)  # Extracts integers and decimals

# Process data rows
data = []
for line in lines:
    numbers = extract_numbers(line)  # Extract only numbers
    if numbers:
        data.append(numbers)

# Ensure data rows match column count
max_columns = len(columns)
for row in data:
    while len(row) < max_columns:
        row.append("")  # Fill missing values with empty strings

# Convert to DataFrame
df = pd.DataFrame(data, columns=columns[:max_columns])  # Trim excess columns

# Save to Excel
output_path = "output02.xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Data successfully saved to {output_path}!")

