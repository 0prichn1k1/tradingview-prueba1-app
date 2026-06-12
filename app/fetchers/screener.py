from tradingview_screener import Query, col, forex, cfd

COLUMNS = ['name', 'close', 'change', 'volume', 'market_cap_basic']


def _fetch_stocks(limit: int = 10, order_by: str = 'change', ascending: bool = False) -> list[dict]:
    try:
        count, df = (
            Query()
            .select(*COLUMNS)
            .where(col('exchange').isin(['NASDAQ', 'NYSE', 'AMEX']))
            .order_by(order_by, ascending=ascending)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def stocks_gainers(limit: int = 10) -> list[dict]:
    return _fetch_stocks(limit, 'change', ascending=False)


def stocks_losers(limit: int = 10) -> list[dict]:
    return _fetch_stocks(limit, 'change', ascending=True)


def stocks_most_active(limit: int = 10) -> list[dict]:
    return _fetch_stocks(limit, 'volume', ascending=False)


def _fetch_forex(limit: int = 10, order_by: str = 'change', ascending: bool = False) -> list[dict]:
    try:
        count, df = (
            forex()
            .select(*COLUMNS)
            .where(col('name').like('USD'))
            .order_by(order_by, ascending=ascending)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def forex_gainers(limit: int = 10) -> list[dict]:
    return _fetch_forex(limit, 'change', ascending=False)


def forex_losers(limit: int = 10) -> list[dict]:
    return _fetch_forex(limit, 'change', ascending=True)


def forex_most_active(limit: int = 10) -> list[dict]:
    return _fetch_forex(limit, 'volume', ascending=False)


def _fetch_cfd(limit: int = 10, order_by: str = 'change', ascending: bool = False) -> list[dict]:
    try:
        count, df = (
            cfd()
            .select(*COLUMNS)
            .order_by(order_by, ascending=ascending)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def cfd_gainers(limit: int = 10) -> list[dict]:
    return _fetch_cfd(limit, 'change', ascending=False)


def cfd_losers(limit: int = 10) -> list[dict]:
    return _fetch_cfd(limit, 'change', ascending=True)


def cfd_most_active(limit: int = 10) -> list[dict]:
    return _fetch_cfd(limit, 'volume', ascending=False)
