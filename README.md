# ERC-20 Real-Time Token Indexer & API

A high-performance, containerized blockchain indexer designed to monitor ERC-20 `Transfer` events in real-time. This system utilizes Python's `multiprocessing` to run a listener and a REST API in parallel, persisting data to a PostgreSQL database for sub-second wallet queries.

---

## 🏗️ Architecture Overview

The system is built with a "Production-First" mindset, separating the data ingestion from the data delivery:

- **Blockchain Listener:** A dedicated process using `Web3.py` that maintains a persistent filter on the Ethereum network.
- **Database:** A PostgreSQL instance optimized with indices on wallet addresses and transaction hashes.
- **REST API:** A `FastAPI` server providing high-concurrency access to indexed data.
- **Containerization:** Fully orchestrated via `Docker Compose` using Alpine Linux to minimize security surface area and image size.

---

## 🚀 Features

- **Real-Time Indexing:** Captures `Transfer` events as they happen on-chain.
- **Parallel Processing:** Uses Python's `multiprocessing` so the API remains responsive while the listener processes blocks.
- **Atomic Persistence:** Ensures balance updates and event logs are synchronized within a single SQL transaction.
- **Auto-Generated Docs:** Full Swagger/OpenAPI documentation available out of the box.
- **Optimized Docker Build:** Multi-stage Alpine builds (~230MB total).

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI (Asynchronous API)
- **Blockchain:** Web3.py
- **Database:** PostgreSQL + SQLAlchemy (ORM)
- **DevOps:** Docker & Docker Compose (Alpine Linux)

---

## 🚦 Getting Started

### 1. Prerequisites

- Docker & Docker Compose installed.
- An Ethereum RPC Provider URL (e.g., Alchemy, Infura, or a local node).

### 2. Environment Setup

Create a `.env` file in the root directory:

```env
RPC_URL=[https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY](https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY)
DATABASE_URL=postgresql://postgres:yourpassword@db:5432/erc20_indexer
```

### 3. Launch the Stack

-Build and start the containers
-docker compose up --build
