from typing import Dict, List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from grafanaapi.schema.grafana import Query, Range, RangeRaw, Search, Target
from placeholder.placeholder import table, create_timeseries

origins = ["http://localhost:3000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/search")
def grafana_search(search: Search):
    return ["table", "timeserie1", "timeserie2"]


@app.post("/query")
def grafana_query(query: Query):
    print(query)
    response = []
    for target in query.targets:
        if target.type == "timeserie":
            if target.target == "timeserie1":
                response.append(create_timeseries(target.target))
            elif target.target == "timeserie2":
                response.append(create_timeseries(target.target))
        elif target.type == "table":
            if target.target == "table":
                response.append(table)
    return response


@app.post("/annotations")
def grafana_annotations():
    pass
