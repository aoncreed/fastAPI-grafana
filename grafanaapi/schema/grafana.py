from pydantic import BaseModel
from typing import Dict, List


class Search(BaseModel):
    target: str


class RangeRaw(BaseModel):
    # from: str
    to: str


class Range(BaseModel):
    # from: str
    to: str
    raw: RangeRaw


class Target(BaseModel):
    target: str
    refId: str
    type: str


class Query(BaseModel):
    app: str
    requestId: str
    timezone: str
    panelId: int
    dashboardId: str = None
    range: dict
    interval: str
    intervalMs: int
    targets: List[Target]
    maxDataPoints: int = None
    scopedVars: dict
    startTime: int
    rangeRaw: RangeRaw
    adhocFilters: list
