import time
import logging
from web3 import Web3
from erc20 import get_erc20_contract

# Setup basic logging to see the output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_event(event):
    """Extracts data from the raw event log."""
    args = event["args"]
    transfer_data = {
        "from": args["from"],
        "to": args["to"],
        "value": args["value"],
        "tx_hash": event["transactionHash"].hex(),
        "block_number": event["blockNumber"],
    }
    logger.info(f"✨ New Transfer Detected: {transfer_data}")


def start_listening(contract_address: str, poll_interval: int = 2):
    """Polls the blockchain for new Transfer events."""
    contract = get_erc20_contract(contract_address)

    # Create a filter for the 'Transfer' event starting from the latest block
    event_filter = contract.events.Transfer.create_filter(from_block="latest")

    logger.info(f"Started listening for events on {contract_address}...")

    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)
