# Market Dashboard — Spec v1

## Qué hace
App web que corre en localhost:5000 y muestra en una sola pantalla
los datos más relevantes de múltiples mercados, actualizándose cada 60 segundos.

## Mercados
- Crypto (via tvscreener + Binance/Bybit)
- Stocks USA (via tvscreener)
- Forex (via tvscreener)
- Commodities (via tvscreener)
- CFD (via tvscreener)

## Secciones de la UI

### 1. Top Gainers / Top Losers
- Top 10 gainers y 10 losers de cada mercado
- Columnas: símbolo, precio actual, cambio % del día
- Filtro por mercado (tabs o dropdown)

### 2. Más Activos
- Top 10 por volumen de cada mercado
- Columnas: símbolo, precio, volumen

### 3. Funding Rates (solo crypto)
- Top 10 con mayor funding rate positivo (longs pagan)
- Top 10 con mayor funding rate negativo (shorts pagan)
- Fuente: Binance Futures + Bybit Linear
- Columnas: símbolo, exchange, funding rate %, próximo funding

## Endpoints del backend
- GET /api/gainers?market=crypto|stocks|forex|commodities
- GET /api/losers?market=crypto|stocks|forex|commodities
- GET /api/most_active?market=crypto|stocks|forex|commodities
- GET /api/funding_rates

## UI
- Fondo oscuro, estilo terminal/trading
- Colores: verde para positivo, rojo para negativo
- Tabla simple, sin gráficos por ahora
- Responsive básico (que entre en pantalla sin scroll horizontal)

## Lo que NO hace (v1)
- No guarda historial
- No tiene alertas
- No muestra gráficos
- No requiere login