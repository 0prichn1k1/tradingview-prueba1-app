from tradingview_screener import crypto, col

COLUMNS = ['name', 'close', 'change', 'volume', 'market_cap_basic']


def _fetch(order_by: str, order_dir: str, limit: int = 10) -> list[dict]:
    try:
        count, df = (
            crypto()
            .select(*COLUMNS)
            .order_by(order_by, order_dir)
            .limit(limit)
            .get_scanner_data()
        )
        return df.to_dict(orient='records')
    except Exception:
        return []


def gainers(limit: int = 10) -> list[dict]:
    return _fetch('change', 'desc', limit)


def losers(limit: int = 10) -> list[dict]:
    return _fetch('change', 'asc', limit)


def most_active(limit: int = 10) -> list[dict]:
    return _fetch('volume', 'desc', limit)
