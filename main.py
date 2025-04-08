from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import user, movie, auth

# O import não utilizado abaixo é necessário, não remover!
from oauth import oauth2_scheme

origins = [
    "http://localhost:5173",
]

app = FastAPI(title="CineMatch API", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exemplo de middleware apenas pra mostar como funciona segundo a documentação
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(movie.router, prefix="/movies", tags=["Movies"])
