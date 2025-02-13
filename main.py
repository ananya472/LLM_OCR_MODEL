import pandas as pd
import re

# Read raw data from text file
with open(r"C:\Users\anany\Desktop\LLM-OCR\output.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize list for structured data
structured_data = []

for line in lines:
    # Remove unwanted characters
    clean_line = re.sub(r'[^\x20-\x7E]', '', line)  # Remove non-ASCII characters
    
    # Replace multiple spaces with a single space
    clean_line = re.sub(r'\s+', ' ', clean_line.strip())
    
    # Split based on single space
    columns = clean_line.split(' ')
    
    # Keep only numerical data (remove text-based entries)
    numerical_columns = [col for col in columns if re.match(r'^\d+(\.\d+)?$', col)]  
    
    if numerical_columns:  # Ensure it's a valid row
        structured_data.append(numerical_columns)

# Convert structured data to DataFrame
df = pd.DataFrame(structured_data)

# Rename columns dynamically as Column1, Column2, etc.
df.columns = [f'Column{i+1}' for i in range(df.shape[1])]

# Save to Excel with correct column headers
df.to_excel("output.xlsx", index=False)

print("Data successfully saved to output.xlsx with proper columns!")


