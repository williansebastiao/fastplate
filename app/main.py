import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
engine = create_engine('mysql+pymysql://fastplate:123456@db/fastplate')
app = FastAPI()


@app.get('/')
def index():
    return {'message': f'{os.getenv("APP_NAME")} is running!'}
