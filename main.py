# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api import customer, items, sites

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(items.router)
# app.include_router(customer.router)
app.include_router(sites.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
