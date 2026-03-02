# test_listener.py
# from listener import start_listening

# # USDC on Sepolia (High activity for testing)
# TEST_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

# if __name__ == "__main__":
#     try:
#         print(f"🚀 Initializing listener for {TEST_CONTRACT}...")
#         start_listening(TEST_CONTRACT)
#     except KeyboardInterrupt:
#         print("\n🛑 Listener stopped by user.")
from db.session import init_db, engine

if __name__ == "__main__":
    try:
        print("🔌 Connecting to Postgres...")
        init_db()
        print("✅ Success! Tables created.")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
