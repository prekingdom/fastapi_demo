from fastapi import FastAPI, Query,Path
from enum import Enum
app =FastAPI(debug=True)

class ModelName(str,Enum):
    alexnet= "alexnet"
    resnet = "resnet"
    lenet = "lenet"
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/item")
async def read_item(skip:int=0,limit:int=0):
    return fake_items_db[skip:skip+limit]


if __name__ == '__main__':
    pass