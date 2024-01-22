from fastapi import FastAPI 


app = FastAPI()

@app.get('/')
def index():
    return "hello World! Ugo"


@app.get('/property/{id}')
def property(id:int):
    return f' This is a Property {id}'

@app.get('/movies')
def movies():
    return {'movies list': {'Movie 1', 'Movie 2', "Movie 3"}}



@app.get('/profile/{username}')
def property(username:str):
    return {f' This is the Profile of  {username}'}