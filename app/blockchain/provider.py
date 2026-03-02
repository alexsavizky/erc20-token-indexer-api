from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()

rpc_url = os.getenv("RPC_URL")
if not rpc_url:
    raise ValueError("❌ RPC_URL is not set in environment variables")

w3 = Web3(Web3.HTTPProvider(rpc_url))

if not w3.is_connected():
    raise ConnectionError("❌ Failed to connect to RPC")

# print("✅ Web3 provider connected")
__all__ = ["w3"]
