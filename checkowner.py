import requests

# Set your APP_ID and API_KEY
APP_ID = "your_app_id"
API_KEY = "your_api_key"

# Set the endpoint URL
url = "https://api.vottun.tech/erc/v1/erc721/ownerOf"

# Set the contract address and token ID of the NFT you want to check
contract_address = "0x1234567890abcdef"
token_id = "12345"

# Set the headers with your APP_ID and API_KEY
headers = {
    "X-APP-ID": APP_ID,
    "X-API-KEY": API_KEY
}

# Set the request parameters
params = {
    "contractAddress": contract_address,
    "tokenId": token_id
}

# Send the GET request to the Vottun API
response = requests.get(url, headers=headers, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Check if you are the owner of the NFT
    if data["owner"] == "your_wallet_address":
        print("Congratulations! You are the owner of the NFT.")
        print("Transaction Hash:", data["transactionHash"])
        print("Token ID:", data["tokenId"])
    else:
        print("Sorry, you are not the owner of the NFT.")
else:
    print("Error:", response.status_code)
