from fastapi import APIRouter, HTTPException
from app.services.movie_service import (
    create_movie,
    get_all,
    get_movie,
    get_movies_by_user,
    update_movie,
    delete_movie,
)
from app.schemas.movie import MovieCreate, MovieResponse

router = APIRouter()


@router.post("/", response_model=MovieResponse)
def register_movie(movie: MovieCreate):
    return create_movie(movie)


@router.get("/", response_model=list[MovieResponse])
def get_all_movies():
    return get_all()


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie_by_id(movie_id: int):
    movie = get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.get("/user/{user_id}", response_model=list[MovieResponse])
def get_movies_by_user_id(user_id: int):
    return get_movies_by_user(user_id)


@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie_by_id(movie_id: int, movie: MovieCreate):
    existing_movie = get_movie(movie_id)
    if not existing_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return update_movie(movie_id, movie)


@router.delete("/{movie_id}")
def delete_movie_by_id(movie_id: int):
    existing_movie = get_movie(movie_id)
    if not existing_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    delete_movie(movie_id)
    return {"message": "Movie deleted successfully"}
