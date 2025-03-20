from pydantic import BaseModel


class MovieCreate(BaseModel):
    id: int | None = None
    title: str
    user_id: int
    rating: float
    genre: str
    review: str


class MovieResponse(BaseModel):
    id: int
    title: str
    user_id: int
    rating: float
    genre: str
    review: str
