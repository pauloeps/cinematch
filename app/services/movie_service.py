from app.models.movie import Movie
from app.schemas.movie import MovieCreate
from app.repository import movie_repository


def create_movie(movie: MovieCreate):
    return movie_repository.create_movie(movie)


def get_all():
    return movie_repository.get_all_movies()


def get_movie(movie_id: int):
    return movie_repository.get_movie(movie_id)


def get_movies_by_user(user_id: int):
    return movie_repository.get_movies_by_user_id(user_id)


def update_movie(movie_id: int, movie: Movie):
    return movie_repository.update_movie(movie_id, movie)


def delete_movie(movie_id: int):
    return movie_repository.delete_movie(movie_id)
