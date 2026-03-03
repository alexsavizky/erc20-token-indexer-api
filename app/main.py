from fastapi import FastAPI
from api.routes import router
from db.session import init_db

app = FastAPI(title="ERC-20 Token Indexer API")


# Initialize tables on startup
@app.on_event("startup")
def startup_event():
    init_db()


# Include our routes
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Indexer is online. Visit /docs for API documentation."}
