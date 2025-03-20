from app.models.movie import Movie
from app.schemas.movie import MovieCreate

movies = []


def create_movie(movie: MovieCreate):
    id = len(movies) + 1
    movie.id = id
    movies.append(movie)
    return movie


def get_all_movies():
    return movies


def get_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            return movie
    return None


def get_movies_by_user_id(user_id: int):
    return [movie for movie in movies if movie.user_id == user_id]


def update_movie(movie_id: int, movie: Movie):
    for i, m in enumerate(movies):
        if m.id == movie_id:
            updated_movie = Movie(
                id=movie_id,
                title=movie.title,
                user_id=movie.user_id,
                rating=movie.rating,
                genre=movie.genre,
                review=movie.review,
            )
            movies[i] = updated_movie
            return updated_movie
    return None


def delete_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return movie
    return None
