from fastapi import FastAPI
from app.api.endpoints import user, movie, auth


app = FastAPI(title="CineMatch API", version="1.0")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(movie.router, prefix="/movies", tags=["Movies"])
