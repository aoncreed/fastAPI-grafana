from datetime import datetime
import pandas as pd
import numpy as np


def create_timeseries(target):
    time_end = datetime.now()
    time_start = time_end - pd.Timedelta("7 days")

    timerange = pd.date_range(start=time_start, end=time_end, freq="H")

    df = pd.DataFrame(timerange, columns=["time"])
    df["data"] = np.random.randint(0, 100, size=len(timerange))
    df["time"] = df["time"].astype(np.int64) // 10**6
    df = df[["data", "time"]]

    split = df.to_dict("split")
    timeserie = {"target": target}
    timeserie["datapoints"] = split.pop("data")

    return timeserie


table = {
    "columns": [
        {"text": "Time", "type": "time"},
        {"text": "Country", "type": "string"},
        {"text": "Number", "type": "number"},
    ],
    "rows": [[1234567, "SE", 123], [1234567, "DE", 231], [1234567, "US", 321],],
    "type": "table",
}
