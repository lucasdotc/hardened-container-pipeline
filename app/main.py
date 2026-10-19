import os

from fastapi import FastAPI

VERSION_FILE = os.path.join(os.path.dirname(__file__), "VERSION")

app = FastAPI()


def _read_version() -> str:
    with open(VERSION_FILE) as f:
        return f.read().strip()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": _read_version()}
