from typing import Optional
from databases import Database
from fastapi import Body, APIRouter, Depends
from datetime import datetime
from app.services import exchange
from app.models import live_latest
from starlette.responses import RedirectResponse
from app.models.rates import Rate
from app.db.repositories.exchange_rate import ExchangeRateRepository
from app.api.dependencies.database import get_repository

router = APIRouter()

@router.get("/")
async def go_home():
    response = RedirectResponse(url='/docs')
    return response

@router.post('/rates/live/latest')
async def get_latest_rates(base: Optional[str] = 'ZAR', currency: Optional[str] = 'USD'):
    data = await exchange.query_rates(None, base, currency)
    return data

@router.post('/rates/db/latest')
async def get_latest_rates_from_db(
base: Optional[str] = 'ZAR', currency: Optional[str] = 'USD',
rate_repository: ExchangeRateRepository = Depends(get_repository(ExchangeRateRepository))
):
    data = await exchange.query_rates(None, base, currency)
    rate_value = data.get('rates')
    new_rate = Rate(symbol=currency, rate=rate_value.get(currency), date=data.get('date'))

    latest_rates = await rate_repository.create_exchange_rate(new_exchange_rate=new_rate)
    return latest_rates

@router.get('/rates/{date}')
async def get_date_rates(date: str = 'YYY-MM-DD'):
    data = await exchange.query_rates(date)
    return data

@router.get('/range')
async def get_range_rates(start_date: Optional[str] = '2020-12-02', end_date: Optional[str] = '2021-01-30'):
    data = await exchange.query_range(start_date, end_date)
    return data