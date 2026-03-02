from dotenv import load_dotenv
import os
import requests

load_dotenv()

rpc_url = os.getenv("RPC_URL")
payload = {"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber"}
headers = {"Content-Type": "application/json"}
response = requests.post(rpc_url, json=payload, headers=headers)
print(response.text)
