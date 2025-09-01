from fastapi import FastAPI

app = FastAPI()

@app.get("/View_Article")
def View():
    return "hello"

@app.post("/Article")
def change():
    return "ddd"

@app.get("/")
def root():
    return " Hi Nane :) "


