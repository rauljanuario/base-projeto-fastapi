from datetime import datetime, UTC

from fastapi import FastAPI

app = FastAPI()


@app.get("/posts/{framework}")
def read_posts(framework):
    return [{"title": f"Criando um aplicação com {framework}", "date": datetime.now(UTC)}]

