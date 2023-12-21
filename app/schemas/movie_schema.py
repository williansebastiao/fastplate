from pydantic import BaseModel

class MovieSchema(BaseModel):
    title: str
    year: int
    genre: str
    plot: str
    photo: str = None