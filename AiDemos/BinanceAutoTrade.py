from binance.client import Client
import time

# replace YOUR_API_KEY and YOUR_SECRET_KEY with your actual API key and secret key
client = Client(api_key='YOUR_API_KEY', api_secret='YOUR_SECRET_KEY')

# set the trading symbol and grid parameters
symbol = 'BTCUSDT'
grid_size = 10  # grid size in USDT
grid_spacing = 1000  # grid spacing in USDT
grid_count = 10  # number of grids

# get the current market price
ticker = client.get_symbol_ticker(symbol=symbol)
last_price = float(ticker['price'])

# calculate the lower and upper bounds of the grid
lower_bound = last_price - (grid_size / 2)
upper_bound = last_price + (grid_size / 2)

# enter the trading loop
while True:
    # get the current market price
    ticker = client.get_symbol_ticker(symbol=symbol)
    last_price = float(ticker['price'])
    
    # if the price goes below the lower bound, place a buy order
    if last_price < lower_bound:
        quantity = (grid_spacing / last_price)
        order = client.create_order(symbol=symbol, side='BUY', type='MARKET', quantity=quantity)
        print(f'Buy order placed: {order}')
        
        # update the grid bounds
        lower_bound -= grid_size
        upper_bound -= grid_size
        
    # if the price goes above the upper bound, place a sell order
    elif last_price > upper_bound:
        quantity = (grid_spacing / last_price)
        order = client.create_order(symbol=symbol, side='SELL', type='MARKET', quantity=quantity)
        print(f'Sell order placed: {order}')
        
        # update the grid bounds
        lower_bound += grid_size
        upper_bound += grid_size
        
    # wait for a few seconds before checking the price again
    time.sleep(5)
