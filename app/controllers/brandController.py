from fastapi import FastAPI

app = FastAPI()

@app.get("/getBrands")
async def getBrands():
    return
