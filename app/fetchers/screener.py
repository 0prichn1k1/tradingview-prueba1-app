from tradingview_screener import Query, col, forex, cfd

COLUMNS = ['name', 'close', 'change', 'volume', 'market_cap_basic']


def _fetch_stocks(limit: int = 10, order_by: str = 'change', order_dir: str = 'desc') -> list[dict]:
    try:
        count, df = (
            Query()
            .select(*COLUMNS)
            .where(col('exchange').isin(['NASDAQ', 'NYSE', 'AMEX']))
            .order_by(order_by, order_dir)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def stocks_gainers(limit: int = 10) -> list[dict]:
    return _fetch_stocks(limit, 'change', 'desc')


def stocks_losers(limit: int = 10) -> list[dict]:
    return _fetch_stocks(limit, 'change', 'asc')


def stocks_most_active(limit: int = 10) -> list[dict]:
    return _fetch_stocks(limit, 'volume', 'desc')


def _fetch_forex(limit: int = 10, order_by: str = 'change', order_dir: str = 'desc') -> list[dict]:
    try:
        count, df = (
            forex()
            .select(*COLUMNS)
            .order_by(order_by, order_dir)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def forex_gainers(limit: int = 10) -> list[dict]:
    return _fetch_forex(limit, 'change', 'desc')


def forex_losers(limit: int = 10) -> list[dict]:
    return _fetch_forex(limit, 'change', 'asc')


def forex_most_active(limit: int = 10) -> list[dict]:
    return _fetch_forex(limit, 'volume', 'desc')


def _fetch_cfd(limit: int = 10, order_by: str = 'change', order_dir: str = 'desc') -> list[dict]:
    try:
        count, df = (
            cfd()
            .select(*COLUMNS)
            .order_by(order_by, order_dir)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def cfd_gainers(limit: int = 10) -> list[dict]:
    return _fetch_cfd(limit, 'change', 'desc')


def cfd_losers(limit: int = 10) -> list[dict]:
    return _fetch_cfd(limit, 'change', 'asc')


def cfd_most_active(limit: int = 10) -> list[dict]:
    return _fetch_cfd(limit, 'volume', 'desc')


# Commodities usa el mismo screener que CFD en TradingView
commodities_gainers = cfd_gainers
commodities_losers = cfd_losers
commodities_most_active = cfd_most_active
