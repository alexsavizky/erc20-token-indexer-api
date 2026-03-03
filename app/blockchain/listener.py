import time
from app.blockchain.erc20 import get_erc20_contract
from app.db.repository import save_transfer_to_db


def handle_event(event):
    args = event["args"]
    return {
        "from": args["from"],
        "to": args["to"],
        "value": args["value"],
        "tx_hash": event["transactionHash"].hex(),
        "block_number": event["blockNumber"],
    }


def start_listening(contract_address: str, poll_interval: int = 2):
    """Polls the blockchain for new Transfer events."""
    contract = get_erc20_contract(contract_address)

    # Create a filter for the 'Transfer' event starting from the latest block
    event_filter = contract.events.Transfer.create_filter(from_block="latest")

    while True:
        for event in event_filter.get_new_entries():
            data = handle_event(event)
            save_transfer_to_db(data)
        time.sleep(poll_interval)
