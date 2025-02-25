import pandas as pd
import re

# File paths
input_file = r"C:\Users\anany\Desktop\LLM-OCR\pages_201_to_300.txt"
output_excel = r"C:\Users\anany\Desktop\LLM-OCR\structured_output02.xlsx"

# Read file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize storage for structured page data
pages = []
current_page = []

# Identify page breaks (assuming '\f' denotes a new page)
for line in lines:
    if "\f" in line:  # Page break detected
        pages.append(current_page)
        current_page = []
    else:
        current_page.append(line.strip())

# Add last page if not empty
if current_page:
    pages.append(current_page)

# Limit to 100 pages
pages = pages[:100]

# Save each page as a separate sheet
with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    for i, page_data in enumerate(pages):
        # Process each line to split into columns
        data_rows = []
        for line in page_data:
            cleaned_line = re.sub(r'[^\x20-\x7E]', '', line)  # Remove non-ASCII
            cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()  # Normalize spaces
            
            # Split into columns
            columns = cleaned_line.split()  # Splitting based on whitespace
            data_rows.append(columns)

        # Find max number of columns
        max_cols = max(len(row) for row in data_rows) if data_rows else 0

        # Ensure all rows have the same number of columns
        for row in data_rows:
            while len(row) < max_cols:
                row.append("")  # Fill missing values with empty string

        # Convert to DataFrame
        df = pd.DataFrame(data_rows)

        # Save to Excel with separate sheets for each page
        sheet_name = f"Page {i+1}"
        df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)

print(f"Structured data successfully saved to {output_excel} ")