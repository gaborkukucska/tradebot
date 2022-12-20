import getpass
import hashlib
import hmac
import requests

def load_plugin(name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, f'plugins/{name}.py')
    plugin = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plugin)
    plugin.main()

# Set up Binance API client
api_key = getpass.getpass('Enter API Key: ')
api_secret = getpass.getpass('Enter API Secret: ')

base_url = 'https://api.binance.com'
endpoint = '/fapi/v1/ticker/price'

# Generate HMAC-SHA256 signature for request
query_string = f'symbol=ETHAUD'
signature = hmac.new(bytes(api_secret, 'latin-1'), msg=bytes(query_string, 'latin-1'), digestmod=hashlib.sha256).hexdigest()

# Send request to Binance API
headers = {'X-MBX-APIKEY': api_key}
response = requests.get(f'{base_url}{endpoint}?{query_string}', headers=headers)

# Validate response and extract buy and sell prices
if response.status_code == 200:
    ticker = response.json()
    bid_price = ticker
