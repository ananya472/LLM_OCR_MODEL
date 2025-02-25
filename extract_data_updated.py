import requests

# API details
API_URL = "https://llmwhisperer-api.us-central.unstract.com/api/v2/whisper-retrieve"
API_KEY = "YOUR_LLM_Whisperer_APIKEY"
WHISPER_HASH = "YOUR_WHISPER_HASH" 

# Headers
headers = {"unstract-key": API_KEY}

# Fetch API response
params = {"whisper_hash": WHISPER_HASH, "page_start": 201, "page_end": 300}  #keep changing it accordingly
response = requests.get(API_URL, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()  # Convert response to JSON format

    # Extract full OCR text
    result_text = data.get("result_text", "")

    # Save to text file
    output_file = r"C:\\Users\\anany\\Desktop\\LLM-OCR\\pages_201_to_300.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result_text)

    print(f"Result text successfully saved to {output_file}")

else:
    print(f"Failed to fetch data, Status Code: {response.status_code}")
    print("Response:", response.text)
