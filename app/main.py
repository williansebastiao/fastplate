import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.controllers.movie_controller import MovieController
from app.schemas.movie_schema import MovieSchema

load_dotenv()
app = FastAPI()


@app.get('/')
def index():
    return {'message': f'{os.getenv("APP_NAME")} is running!'}


@app.get('/api/movies')
def find_all_movies():
    movie = MovieController()
    return movie.find_all()

@app.get('/api/movies/{id}')
def find_movie_by_id(id):
    movie = MovieController()
    return movie.find_by_id(id)

@app.post('/api/movies/store')
def store_movies(data: MovieSchema):
    movie = MovieController()
    return movie.store(data)
