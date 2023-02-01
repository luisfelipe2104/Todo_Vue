from fastapi import FastAPI
from routes.task import task
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload

app = FastAPI()
app.include_router(task)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task)
