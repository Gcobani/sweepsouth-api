from app.db.repositories.base import BaseRepository
from app.models.rates import Rate
CREATE_EXCHANGE_RATE_QUERY = """
    INSERT INTO exchange_rates (symbol, rate, date)
    VALUES (:symbol, :rate, :date)
    RETURNING id, symbol, rate, date;
"""
class ExchangeRateRepository(BaseRepository):
    async def create_exchange_rate(self, *, new_exchange_rate: Rate) -> Rate:
        query_values = new_exchange_rate.dict()
        print(self.db)
        exchange = await self.db.fetch_one(query=CREATE_EXCHANGE_RATE_QUERY, values=query_values)
        return Rate(**exchange)