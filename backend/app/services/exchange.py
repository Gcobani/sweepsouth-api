import httpx

BASE_URL = 'https://api.exchangeratesapi.io/'

async def client_fetch(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        res.raise_for_status()
        print(res.json())
    return res.json()

async def query_rates(date = None , base = None , currency = None):
    url = BASE_URL
    if date is None:
        url += 'latest'
    else:
        url += f'{date}'

    if base is None:
        url += f'?base=ZAR'
    else:
        url += f'?base={base}'

    if currency:
        url += f'&symbols={currency}'
    return await client_fetch(url)


async def query_range(start_date, end_date):
    url = BASE_URL
    url += f'history?start_at={start_date}'
    if end_date:
        url += f'&end_at={end_date}'
    return await client_fetch(url)