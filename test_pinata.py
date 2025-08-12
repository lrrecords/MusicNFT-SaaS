import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_KEY")
}
with open("test.txt", "w") as f:
    f.write("test")
files = {"file": ("test.txt", open("test.txt", "rb"))}
response = requests.post(url, headers=headers, files=files)
print(response.json())