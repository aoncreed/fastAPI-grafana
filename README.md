# FastAPI for Grafana

This is a simple test API for the grafana datasource extension SimpleJSON

## Install

Clone this project

Install the dependencies listed in Pipfile

```bash
pipenv install
```

## Run

Run fastAPI with uvicorn

```bash
uvicorn grafanaapi.main:app --reload
```

Run grafana in docker with simpleJSON datasource installed

```bash
docker run -d \
--name grafana \
-p 3000:3000 \
-e "GF_INSTALL_PLUGINS=grafana-simple-json-datasource" \
grafana/grafana
```
