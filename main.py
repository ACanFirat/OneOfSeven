from fastapi import FastAPI
from db.database import Base, engine
from router import users, ledger
import uvicorn
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(ledger.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
