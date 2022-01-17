from fastapi import FastAPI
import uvicorn
import re

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Duke Student"}


@app.get("/dukeid/{string}")
async def dukeid(string: str):
    """check if id is valid"""

    if len(string) == 5 and re.findall("^[a-zA-Z0-9]+$", string):
        return "Valid"
    else:
        return "Not valid"


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
