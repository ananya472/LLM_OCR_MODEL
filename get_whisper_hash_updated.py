import requests
import time

# API details
API_URL = "https://llmwhisperer-api.us-central.unstract.com/api/v2/whisper"
API_KEY = "YOUR_LLM_Whisperer_APIKEY"

headers = {
    "unstract-key": API_KEY,
    "Content-Type": "application/octet-stream"
}

# Path to the PDF file
file_path = r"C:\Users\anany\Desktop\LLM-OCR\822_Construction Test Data Volume 1 (2) (1)-compressed-pages-deleted-compressed-pages-deleted.pdf"

try:
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{API_URL}?mode=form&output_mode=layout_preserving",
            headers=headers,
            data=file
        )

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        whisper_hash = data.get("whisper_hash")

        if whisper_hash:
            print(f"Whisper Hash: {whisper_hash}")
        else:
            print("Failed to extract whisper_hash from response.")
    else:
        print(f"Failed to process the PDF. Response: {response.text}")

except Exception as e:
    print("An error occurred:", str(e))
