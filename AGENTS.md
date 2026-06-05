\# Proyecto: Market Dashboard

App web local (Flask + HTML) que muestra datos de mercado en tiempo real.



\# Stack

\- Backend: Python 3.10+ con Flask

\- Screener: librería `tradingview-screener`

\- Funding rates: APIs públicas de Binance y Bybit (sin API key)

\- Frontend: HTML/CSS/JS vanilla en un solo archivo (app/static/index.html)

\- Sin base de datos, sin autenticación, sin dependencias de pago



\# Estructura

\- app/main.py → servidor Flask, sirve endpoints JSON y el index.html

\- app/fetchers/crypto.py → gainers/losers/activos crypto vía tvscreener

\- app/fetchers/screener.py → stocks USA, forex, commodities, CFD vía tvscreener

\- app/fetchers/funding.py → funding rates de Binance y Bybit

\- app/static/index.html → UI, consume los endpoints del backend vía fetch()



\# Reglas

\- Leer spec en docs/spec.md antes de escribir cualquier código

\- Cada endpoint Flask devuelve JSON limpio

\- El frontend se refresca automáticamente cada 60 segundos

\- Manejo de errores en todos los fetchers (si una API falla, devuelve lista vacía)

\- Comentarios en español

\- No usar librerías pagas ni que requieran API key

