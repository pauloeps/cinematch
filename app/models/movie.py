from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    user_id: int
    rating: float
    genre: str
    review: str
