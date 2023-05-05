from fastapi import FastAPI
from processor import *
from json_encoder import ORJSONResponse
from fastapi.responses import HTMLResponse

#from pydantic import BaseModel
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/")
def documentation():
    return HTMLResponse("""<h1>Now you are on documentation route</h1>
    <ul>
    <li>route "/songs-video" -- show you songs with video on YouTube</li>
    <li>route "/sort-values" -- show you songs, which sorted by some columns</li>
    <li>route "/search-columns" -- show you songs only with individually columns</li>
    </ul>""")


@app.get("/songs-video")
def show_url_videos(skip: int = 0, limit: int = 10):
    return open_youtube()


@app.get("/sort-values")
def sort_values(skip: int = 0, limit: int = 10):
    # json_compatible_item_data = jsonable_encoder(sort())
    return sort()
    # return JSONResponse(content=json_compatible_item_data)
    # return sort()


@app.get("/search-columns")
def show_url_videos(skip: int = 0, limit: int = 10):
    return search()


@app.get("/test-route")
def testing():
    return test_pretty()
