from tradingview_screener import crypto, col

STABLECOINS = ['USDT', 'USDC', 'BUSD', 'DAI', 'TUSD', 'FDUSD', 'USDP']
COLUMNS = ['name', 'close', 'change', 'volume', 'market_cap_calc']


def _fetch(order_by: str, ascending: bool, limit: int = 10) -> list[dict]:
    try:
        conditions = [
            col('exchange.tr') == 'Binance',
            col('market_cap_calc') > 50_000_000,
        ]
        for sc in STABLECOINS:
            conditions.append(col('name').not_like(sc))

        count, df = (
            crypto()
            .select(*COLUMNS)
            .where(*conditions)
            .order_by(order_by, ascending=ascending)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def gainers(limit: int = 10) -> list[dict]:
    return _fetch('change', ascending=False, limit=limit)


def losers(limit: int = 10) -> list[dict]:
    return _fetch('change', ascending=True, limit=limit)


def most_active(limit: int = 10) -> list[dict]:
    return _fetch('volume', ascending=False, limit=limit)
