Master Prompt – Build a Production-Grade Algorithmic Trading Platform

You are an expert Quantitative Developer, Software Architect, Senior Python/FastAPI Engineer, and Trading Systems Expert.

Your objective is to design and implement a production-ready, enterprise-grade algorithmic trading platform with a modular, scalable, plug-and-play architecture. The system should support multiple brokers, multiple exchanges, paper trading, live trading, backtesting, AI-assisted analysis, and extensibility for future strategies and integrations.

---

Core Objectives

The platform must:

- Fetch historical and real-time market data.
- Support paper trading and live trading.
- Execute automated strategies.
- Perform historical backtesting.
- Monitor portfolios and positions.
- Enforce configurable risk management.
- Provide REST APIs and WebSocket endpoints.
- Support multiple brokers through a common interface.
- Allow strategies to be added without changing core code.
- Be cloud-native and production-ready.

---

Technology Stack

Backend:

- Python 3.13+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- APScheduler / Celery
- RabbitMQ / Kafka (optional)

Frontend:

- React
- TypeScript
- TradingView Lightweight Charts

Authentication:

- JWT
- OAuth2 (optional)

Deployment:

- Docker
- Kubernetes
- GitHub Actions

Documentation:

- Swagger/OpenAPI

Testing:

- PyTest
- Integration Tests
- Mock Broker APIs

---

High-Level Architecture

Design the following services:

- API Gateway
- Authentication Service
- User Service
- Broker Service
- Market Data Service
- Strategy Engine
- Indicator Engine
- Signal Engine
- Risk Management Engine
- Order Management System (OMS)
- Portfolio Service
- Position Service
- Backtesting Engine
- Paper Trading Engine
- Notification Service
- AI Assistant Service
- Reporting Service
- Scheduler Service
- Audit & Logging Service

Explain communication between services and provide an architecture diagram.

---

Project Structure

Generate a clean folder structure using Clean Architecture and Domain-Driven Design (DDD).

Separate:

- API
- Domain
- Application
- Infrastructure
- Database
- Strategies
- Indicators
- Brokers
- Notifications
- Tests
- Configuration

---

User Management

Implement:

- Registration
- Login
- JWT Authentication
- Refresh Tokens
- Role-Based Access (Admin, Trader, Viewer)

---

Broker Integration

Design a common broker interface:

BrokerInterface
login()
logout()
refresh_token()
get_profile()
get_balance()
get_margin()
get_holdings()
get_positions()
get_orders()
place_order()
modify_order()
cancel_order()
subscribe_market_data()
unsubscribe_market_data()

Use the Adapter Pattern so new brokers can be added by implementing only this interface.

---

Market Data Engine

Support:

- Historical OHLC data
- Tick-by-tick data
- WebSocket streaming
- Candle generation
- Timeframe aggregation (1m, 5m, 15m, 1h, 1d)
- Corporate actions
- Holiday calendar
- Instrument master

---

Indicator Engine

Support 100+ indicators including:

Trend:

- EMA
- SMA
- WMA
- HMA
- MACD
- Supertrend
- ADX
- Ichimoku

Momentum:

- RSI
- Stochastic
- Stochastic RSI
- ROC
- CCI
- Williams %R

Volatility:

- ATR
- Bollinger Bands
- Keltner Channel
- Donchian Channel

Volume:

- VWAP
- Anchored VWAP
- OBV
- MFI
- CMF
- Volume Profile

Other:

- Fibonacci
- Pivot Points
- PSAR
- Linear Regression
- Heikin Ashi
- Renko

---

Strategy Engine

Every strategy must implement:

initialize()
on_start()
on_new_tick()
on_new_candle()
generate_signal()
validate_signal()
manage_position()
exit_signal()
cleanup()

Strategies must be configurable from the database without code changes.

---

Trading Strategies

Trend Following

- EMA Crossover
- SMA Crossover
- Triple EMA
- Golden Cross / Death Cross
- Supertrend
- MACD Crossover
- Moving Average Ribbon
- ADX Trend
- Donchian Breakout
- Ichimoku Cloud

Momentum

- RSI Reversal
- RSI Divergence
- MACD Histogram
- ROC
- Stochastic
- Stochastic RSI
- CCI
- Williams %R
- Awesome Oscillator

Mean Reversion

- Bollinger Bands
- VWAP Mean Reversion
- Moving Average Reversion
- Z-Score Reversion

Breakout

- Opening Range Breakout
- Previous Day High/Low
- ATR Breakout
- Volume Breakout
- Pivot Breakout
- Consolidation Breakout
- Darvas Box

Price Action

- Support/Resistance
- Swing High/Low
- Trendline Breakout
- Market Structure
- Supply/Demand
- Liquidity Sweep

Smart Money Concepts

- Order Blocks
- Fair Value Gap
- Break of Structure
- Change of Character
- Liquidity Grab
- Institutional Candle Detection

Candlestick

- Engulfing
- Hammer
- Doji
- Morning Star
- Evening Star
- Pin Bar
- Three White Soldiers
- Three Black Crows

Intraday

- Gap Up
- Gap Down
- VWAP Bounce
- Opening Momentum
- Scalping
- Afternoon Breakout

Swing

- Pullback
- Fibonacci Retracement
- Flag
- Pennant
- Cup & Handle
- Ascending Triangle
- Descending Triangle

Quantitative

- Pairs Trading
- Statistical Arbitrage
- Cointegration
- Beta Neutral
- Factor Investing
- Momentum Investing

Machine Learning

- Random Forest
- XGBoost
- LSTM
- Reinforcement Learning
- Sentiment Analysis

---

Signal Engine

Implement:

- Buy Signals
- Sell Signals
- Hold Signals
- Confidence Score
- Multi-Timeframe Confirmation
- Indicator Confirmation
- Volume Confirmation

---

Risk Management

Implement configurable rules:

- Maximum daily loss
- Maximum weekly loss
- Maximum monthly loss
- Maximum drawdown
- Maximum open positions
- Position sizing
- Kelly Criterion
- ATR Stop Loss
- Trailing Stop
- Time Exit
- Volatility Exit
- Profit Booking
- Portfolio Exposure
- Sector Exposure
- Consecutive Loss Protection
- Trading Session Rules
- News Blackout
- Holiday Rules

Every order must pass through the Risk Engine before execution.

---

Order Management System (OMS)

Support:

- Place Order
- Modify Order
- Cancel Order
- Market Orders
- Limit Orders
- Stop Orders
- Bracket Orders
- Cover Orders
- Partial Fills
- Slippage
- Retry Logic
- Order Lifecycle Tracking

---

Portfolio Management

Track:

- Holdings
- Open Positions
- Closed Positions
- Daily P&L
- Realized P&L
- Unrealized P&L
- Brokerage
- Taxes
- ROI
- CAGR
- Portfolio Allocation

---

Backtesting Engine

Input:

- Historical Data
- Strategy
- Capital
- Date Range

Output:

- Win Rate
- Profit Factor
- Drawdown
- Sharpe Ratio
- Sortino Ratio
- CAGR
- Equity Curve
- Trade Log
- Monthly Reports

---

Paper Trading

Support:

- Virtual Balance
- Virtual Orders
- Live Market Feed
- Strategy Testing
- Portfolio Tracking

Switch between Paper and Live using configuration only.

---

Notification Service

Support:

- Email
- Telegram
- Slack
- Push Notifications

Notify for:

- Entry
- Exit
- Stop Loss
- Errors
- Daily Summary
- Weekly Summary

---

Dashboard

Display:

- Live Charts
- Watchlist
- Orders
- Holdings
- Positions
- P&L
- Strategies
- Backtest Reports
- Risk Metrics
- Notifications

---

Database Design

Generate schemas for:

- Users
- Brokers
- Instruments
- Strategies
- Indicators
- Watchlists
- Orders
- Trades
- Positions
- Holdings
- Backtests
- Notifications
- Audit Logs
- Sessions

---

API Design

Generate REST APIs and WebSocket endpoints for all modules.

Include:

- Swagger
- Request/Response Models
- Validation
- Error Handling

---

Logging & Monitoring

Implement:

- Structured Logging
- Correlation IDs
- Metrics
- Health Checks
- Prometheus
- Grafana
- Audit Trail

---

Security

Implement:

- JWT
- OAuth2
- API Keys
- Secret Management
- Encryption
- Input Validation
- Secure Headers
- Rate Limiting
- IP Whitelisting

---

Design Patterns

Use:

- Strategy
- Factory
- Abstract Factory
- Adapter
- Facade
- Repository
- Unit of Work
- Builder
- Singleton
- Observer
- Command
- Mediator
- Template Method
- Chain of Responsibility
- Decorator
- Dependency Injection

---

Enterprise Patterns

Use:

- Clean Architecture
- Domain-Driven Design (DDD)
- CQRS
- Event-Driven Architecture
- Event Bus
- Outbox Pattern
- Saga Pattern
- Retry Pattern
- Circuit Breaker
- Bulkhead Isolation
- Dead Letter Queue
- Idempotent Order Processing

---

AI Module

Implement an AI assistant capable of:

- Explaining why trades were executed.
- Summarizing daily and weekly portfolio performance.
- Converting natural-language strategy descriptions into executable strategy configurations.
- Recommending strategy parameter tuning based on historical backtesting results.
- Detecting anomalous trading behavior or excessive risk.

---

Code Quality

Follow:

- SOLID Principles
- DRY
- KISS
- YAGNI
- Type Hints
- Async Programming
- Pydantic Validation
- Comprehensive Unit & Integration Tests

---

Output Requirements

Generate the implementation module by module.

For every module include:

1. Purpose
2. Architecture
3. Folder Structure
4. Database Models
5. API Contracts
6. Business Logic
7. Design Patterns Used
8. Complete Production-Ready Code
9. Unit Tests
10. Integration Tests
11. Deployment Configuration
12. Documentation
13. Future Extension Points

Do not skip implementation details. Assume this project will be used in a real trading environment and optimize for maintainability, scalability, security, observability, and extensibility.