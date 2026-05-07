from typing import List
from fastapi import FastAPI
from db import  SessionDep, create_all_tables
from sqlmodel import select
from operations import showdog, createdog
from model import Dogsid,Dog

app = FastAPI(lifespan=create_all_tables)

@app.post("/dogcreated",response_model=Dogsid)
async def createssgod(dogs: Dog, session:SessionDep):
    return createdog(dogs, session)


@app.get("/showdogall",response_model=list[Dogsid])
async def showdogalls(session:SessionDep):
    return showdog(session)


