from sqlalchemy.orm import Session
from sqlalchemy import select
from app.config.database import engine
from app.models.movie import Movie

class MovieController:

    def __init__(self):
        ...

    def store(self, data):
        with Session(engine) as session:
            movie = Movie(
                title=data.title,
                year=data.year,
                genre=data.genre,
                plot=data.plot,
                photo=data.photo
            )
            session.add(movie)
            session.commit()

            response = session.query(Movie).get(movie.id)
            return response

    def find_all(self):
        with Session(engine) as session:
            query = session.query(Movie).filter(Movie.deleted_at == None).order_by(Movie.id.desc())
            movies = query.all()

            return movies

    def find_by_id(self, id):
        with Session(engine) as session:
            query = session.query(Movie).filter(Movie.id == id, Movie.deleted_at == None)
            movie = query.first()

            return movie

    def destroy(self, id):
        ...