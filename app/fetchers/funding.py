import requests

BINANCE_URL = 'https://fapi.binance.com/fapi/v1/premiumIndex'
BYBIT_URL = 'https://api.bybit.com/v5/market/tickers'


def _get_binance() -> list[dict]:
    try:
        r = requests.get(BINANCE_URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        result = []
        for item in data:
            rate = float(item.get('lastFundingRate', 0))
            if rate == 0:
                continue
            result.append({
                'symbol': item['symbol'],
                'exchange': 'Binance',
                'fundingRate': rate,
                'nextFundingTime': item.get('nextFundingTime', 0),
            })
        return result
    except Exception:
        return []


def _get_bybit() -> list[dict]:
    try:
        r = requests.get(BYBIT_URL, params={'category': 'linear'}, timeout=10)
        r.raise_for_status()
        data = r.json()
        tickers = data.get('result', {}).get('list', [])
        result = []
        for item in tickers:
            rate = float(item.get('fundingRate', 0))
            if rate == 0:
                continue
            result.append({
                'symbol': item['symbol'],
                'exchange': 'Bybit',
                'fundingRate': rate,
                'nextFundingTime': int(item.get('nextFundingTime', 0)),
            })
        return result
    except Exception:
        return []


def get_all() -> dict[str, list[dict]]:
    binance = _get_binance()
    bybit = _get_bybit()

    all_rates = sorted(binance + bybit, key=lambda x: x['fundingRate'], reverse=True)

    positives = [r for r in all_rates if r['fundingRate'] > 0][:10]
    negatives = [r for r in all_rates if r['fundingRate'] < 0][-10:]
    negatives.reverse()

    return {'positive': positives, 'negative': negatives}
