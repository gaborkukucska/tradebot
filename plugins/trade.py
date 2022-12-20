def trade(direction):
    if direction == 'buy':
        # Place a buy order for ETH using 100% of the funds in the AUD wallet
        endpoint = '/fapi/v1/order'
        query_string = f'symbol=ETHAUD&side=BUY&type=MARKET&quantity=100&timestamp={int(time.time() * 1000)}&signature={signature}'
        headers = {'X-MBX-APIKEY': api_key}
        response = requests.post(f'{base_url}{endpoint}?{query_string}', headers=headers)
        if response.status_code == 200:
            print('Trade successful')
        else:
            print('Error placing trade')
    elif direction == 'sell':
        # Place a sell order for ETH using 100% of the funds in the ETH wallet
        endpoint = '/fapi/v1/order'
        query_string = f'symbol=ETHAUD&side=SELL&type=MARKET&quantity=100&timestamp={int(time.time() * 1000)}&signature={signature}'
        headers = {'X-MBX-APIKEY': api_key}
        response = requests.post(f'{base_url}{endpoint}?{query_string}', headers=headers)
        if response.status_code == 200:
            print('Trade successful')
        else:
            print('Error placing trade')
