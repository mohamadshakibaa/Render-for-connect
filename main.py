from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

class ArticleCreate(BaseModel):
        title: str
        author: str
        year: int

class Article(ArticleCreate):
    id: int

article_db = {}

@app.get("/")
def root():
    return " Hi Nane :) "

@app.get("/view_Articles/" , response_model=list[Article])
async def read_article(): 
    return list(article_db.values())

@app.get("/Articles/{article_id}" , response_model= Article)
async def read_article(article_id : int):
    if article_id not in article_db :
        raise  HTTPException(status_code= 404 , detail="Article not found")
    return article_db[article_id]

@app.post("/Articles/" , response_model= Article)
async def create_article(article : ArticleCreate):
    new_id = len(article_db) + 1
    new_article = Article(id=new_id , **article.dict())
    article_db[new_id] = new_article
    return new_article

@app.put("/Article/{article_id}" , response_model=Article)
async def update_article(article_id : int , article : ArticleCreate):
    if article_id not in article_db:
        raise HTTPException (status_code= 404 , detail="article NOT found")
    update_article = Article(id=article_id , **article.dict())
    article_db[article_id] = update_article
    return update_article

@app.delete("/Article/{article_id}")
async def delete_article(article_id : int):
    if article_id not in article_db:
        raise HTTPException(status_code=404 , detail= "Article not found for delete")
    del article_db[article_id]
    return {"messaeg" : "Article deleted successfully"}

