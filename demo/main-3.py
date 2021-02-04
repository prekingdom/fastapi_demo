from fastapi import Depends,FastAPI,Header,HTTPException

async def verify_token(x_token:str=Header(...,convert_underscores=False)):
    if x_token!="token_new":
        raise HTTPException(status_code=400,detail=" token hahah")

async def verify_key(x_key:str=Header(...,convert_underscores=False)):
    if x_key!="key_new":
        raise HTTPException(status_code=400,detail="key hahah")


app = FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])


@app.get("/items")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]