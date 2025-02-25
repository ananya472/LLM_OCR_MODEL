# LLM_OCR_MODEL
# Converting Handwritten PDF to Excel
This project focuses on extracting text from a handwritten PDF, processing it, and converting it into a structured Excel file. The workflow is divided into three main scripts:


get_whisper_hash_updated.py – Sends a PDF to the API, retrieves the Whisper Hash, and stores it for later data retrieval.

extract_data_updated.py – Extracts text or structured data from the API response and processes it for further use.

main_updated.py –  Cleans and structures the text before saving it in an Excel file.

final_result.xlsx – The final processed data stored in an Excel shee




get_whisper_hash.py – Handles the PDF upload and sends it to the OCR API.
extract_data.py – Retrieves the processed text using a unique identifier (whisper hash).
main.py – Cleans and structures the text before saving it in an Excel file.

# Project Workflow
# 1. Uploading and Processing the PDF (get_whisper_hash.py)
The script takes a handwritten PDF ("samplepdf_250204_185538.pdf" in this case) and sends it to the LLM Whisperer API for processing.
The API performs OCR (Optical Character Recognition) to extract text while preserving layout.
A whisper hash (unique identifier) is returned, which is used to retrieve the extracted text later.

# 2. Retrieving Extracted Text (extract_data.py)
Using the whisper hash, this script fetches the processed text from the API.
The extracted content is stored in output.txt, ensuring that only meaningful text is saved.

# 3. Cleaning and Structuring the Data (main.py)
The raw extracted text often contains unwanted characters and irregular spacing.
Text preprocessing is performed using regular expressions (regex):
Removes non-ASCII characters and unwanted symbols.
Converts multiple spaces into single spaces for better readability.
Extracts numerical values separately to form structured data.
The cleaned data is stored in a pandas DataFrame, dynamically assigning column names.
Finally, the structured data is exported to an Excel file (output.xlsx).

# To run the project, follow these steps:

Install Dependencies
First, install all the required packages by running the following command:
pip install -r requirements.txt

Upload and Process the PDF
Run get_whisper_hash.py to send the handwritten PDF to the OCR API. This script will return a unique identifier (whisper hash) for retrieving the processed text.
Command: python get_whisper_hash.py

Retrieve Extracted Text
Use extract_data.py to fetch the processed text using the whisper hash. The extracted text will be saved in a file named output.txt.
Command: python extract_data.py

Clean and Convert Data to Excel
Finally, run main.py to clean the text, structure it into columns, and save it as an Excel file. The final output will be stored as output.xlsx.
Command: python main.py
