import json
from pathlib import Path
from web3 import Web3
from provider import w3

ABI_PATH = Path(__file__).parent / "abis" / "erc20.json"


def load_abi():
    with open(ABI_PATH, "r") as f:
        return json.load(f)


ERC20_ABI = load_abi()


def get_erc20_contract(address: str):
    """Initializes the contract instance using the loaded ABI."""
    checksum_address = Web3.to_checksum_address(address)
    return w3.eth.contract(address=checksum_address, abi=ERC20_ABI)


def get_token_metadata(contract):
    """Fetches basic token info to verify the connection."""
    return {
        "name": contract.functions.name().call(),
        "symbol": contract.functions.symbol().call(),
        "decimals": contract.functions.decimals().call(),
    }


print(
    get_token_metadata(get_erc20_contract("0x6B175474E89094C44Da98b954EedeAC495271d0F"))
)
