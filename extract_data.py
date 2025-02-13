import requests
import json

# API details
API_URL = "https://llmwhisperer-api.us-central.unstract.com/api/v2/whisper-retrieve"
API_KEY = "YOUR_LLM_Whisperer_APIKEY"
WHISPER_HASH = "YOUR_WHISPER_HASH" # you'll get it as a result after running get_whisper_hash.py

# Headers
headers = {"unstract-key": API_KEY}

# Fetch API response
params = {"whisper_hash": WHISPER_HASH}
response = requests.get(API_URL, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()  # Convert response to JSON format

    # Extract only "result_text"
    result_text = data.get("result_text", "")

    
    output_file = "output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result_text) 

    print(f"Result text successfully saved to {output_file} ✅")
else:
    print(f"Failed to fetch data , Status Code: {response.status_code}")
    print("Response:", response.text)


