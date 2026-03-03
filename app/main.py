from fastapi import FastAPI
from app.api.routes import router
from app.db.session import init_db
import multiprocessing
from app.blockchain.listener import start_listening
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="ERC-20 Token Indexer API")
TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")


def run_listener():
    """Wrapper function to run the listener process."""
    print("🛰️ Starting Blockchain Listener Process...")
    start_listening(TOKEN_ADDRESS)


@app.on_event("startup")
def startup_event():
    # 1. Initialize DB tables
    init_db()

    # 2. Start the listener in a separate process
    proc = multiprocessing.Process(target=run_listener, daemon=True)
    proc.start()


app.include_router(router)
