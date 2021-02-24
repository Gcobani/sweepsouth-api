import pytest

from httpx import AsyncClient
from fastapi import FastAPI

from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY


class TestCleaningsRoutes:

    # TEST /api/rates/live/latest
    @pytest.mark.asyncio
    async def test_live_route_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post('/api/rates/live/latest', json={})
        assert res.status_code != HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_live_route_response(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post('/api/rates/live/latest', json={'base':'ZAR', 'currency':'USD'})
        assert list(res.json().keys()) == ['rates', 'base', 'date']
    #
    # TEST /api/rates/db/latest
    @pytest.mark.asyncio
    async def test_db_route_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post('/api/rates/db/latest', json={})
        assert res.status_code != HTTP_404_NOT_FOUND

    # TEST /api/rates/{date}
    @pytest.mark.asyncio
    async def test_date_route_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get('/api/rates/2020-01-01')
        assert res.status_code != HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_date_route_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get('/api/rates/2020-01-01')
        isPassing = False
        if list(res.json().keys()) == ['rates', 'base', 'date']:
            isPassing = True
        else:
            isPassing = False

        if len(res.json().get('rates')) > 1 and isPassing:
            isPassing = True
        else:
            isPassing = False

        assert isPassing


    @pytest.mark.asyncio
    async def test_range_route_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get('/api/range')
        assert res.status_code != HTTP_404_NOT_FOUND

    @pytest.mark.asyncio
    async def test_range_route_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get('/api/range?start_date=2020-01-01&end_date=2021-01-03')
        isFailing = True

        if list(res.json().keys()) == ['rates', 'start_at', 'base', 'end_at']:
            isFailing = False
        else:
            isFailing = True

        if len(res.json().get('rates').get('2020-01-02')) > 1 and len(res.json().get('rates').get('2020-01-03')) > 1 and not isFailing:
            isFailing = False
        else:
            isFailing = True

        assert not isFailing
