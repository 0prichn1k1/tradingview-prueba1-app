from flask import Flask, jsonify, request, send_from_directory

from .fetchers import crypto, screener, funding

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)


@app.route('/api/gainers')
def api_gainers():
    market = request.args.get('market', 'crypto')
    limit = int(request.args.get('limit', 10))

    fetchers = {
        'crypto': crypto.gainers,
        'stocks': screener.stocks_gainers,
        'forex': screener.forex_gainers,
        'commodities': screener.commodities_gainers,
        'cfd': screener.cfd_gainers,
    }

    fetcher = fetchers.get(market)
    if fetcher is None:
        return jsonify({'error': f'Unknown market: {market}'}), 400

    return jsonify(fetcher(limit))


@app.route('/api/losers')
def api_losers():
    market = request.args.get('market', 'crypto')
    limit = int(request.args.get('limit', 10))

    fetchers = {
        'crypto': crypto.losers,
        'stocks': screener.stocks_losers,
        'forex': screener.forex_losers,
        'commodities': screener.commodities_losers,
        'cfd': screener.cfd_losers,
    }

    fetcher = fetchers.get(market)
    if fetcher is None:
        return jsonify({'error': f'Unknown market: {market}'}), 400

    return jsonify(fetcher(limit))


@app.route('/api/most_active')
def api_most_active():
    market = request.args.get('market', 'crypto')
    limit = int(request.args.get('limit', 10))

    fetchers = {
        'crypto': crypto.most_active,
        'stocks': screener.stocks_most_active,
        'forex': screener.forex_most_active,
        'commodities': screener.commodities_most_active,
        'cfd': screener.cfd_most_active,
    }

    fetcher = fetchers.get(market)
    if fetcher is None:
        return jsonify({'error': f'Unknown market: {market}'}), 400

    return jsonify(fetcher(limit))


@app.route('/api/funding_rates')
def api_funding_rates():
    return jsonify(funding.get_all())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
