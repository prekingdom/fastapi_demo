from fastapi import FastAPI, Query,Path
from enum import Enum
app =FastAPI(debug=True)

class ModelName(str,Enum):
    alexnet= "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/modles/{model_name}")
async def read_item(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name":model_name,"message":"Deep learning FTW!"}
    if model_name ==model_name.resnet:
        return {"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name":model_name,"message":"Have some residuals"}

if __name__ == '__main__':
    print(ModelName.lenet3.value)
    print(ModelName.lenet3.name)