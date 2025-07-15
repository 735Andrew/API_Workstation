from typing import Dict
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from app.models import Forecast
from app.data.forecast import test_data_create, forecast_get, forecast_add

router = APIRouter()


@router.get("/ping", status_code=200)
def pong_get():
    return HTMLResponse("PONG")


@router.get("/health", status_code=200)
def health_get() -> Dict:
    return {"status": "HEALTHY"}


@router.get("/list", status_code=200)
def list_get():
    test_data_create()
    try:
        return HTMLResponse(forecast_get())
    except Exception as exc:
        raise HTTPException(status_code=400, detail=exc)


@router.post("/forecast", status_code=201)
def forecast_post(data: Forecast):
    try:
        return forecast_add(data)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=exc)
