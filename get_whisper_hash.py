import requests

API_URL = "https://llmwhisperer-api.us-central.unstract.com/api/v2/whisper"
API_KEY = "YOUR_LLM_Whisperer_APIKEY"

headers = {
    "unstract-key": API_KEY,
    "Content-Type": "application/octet-stream"
}

file_path = r"C:\Users\anany\Desktop\LLM-OCR\samplepdf_250204_185538.pdf"

try:
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{API_URL}?mode=form&output_mode=layout_preserving",
            headers=headers,
            data=file
        )

    print(f"Status Code: {response.status_code}")
    print("Response:", response.text)

except Exception as e:
    print("An error occurred:", str(e))

