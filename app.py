from fastapi import FastAPI, HTTPException, Request
import uvicorn
import search_web 
import scrape_content


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}   


@app.get("/search/{query}")
async def search(query: str):
    return search_web.search(query)


@app.get("/scrape/{url}")
async def scrape(url: str):
    return scrape_content.scrape(url)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    # app.run(host="0.0.0.0", port=8000)
