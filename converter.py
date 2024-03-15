import requests

API_KEY = 'fca_live_oqUBX8mCmAkRLOfzz2awBso9qhr2FAwpl2ccAxLd'

BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD',"CAD",'AUD','JPY','KRW','CNY']
def convert_currency(value):
    currencies_list = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={value}&currencies={currencies_list}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print("Invalid currency.")
        return None

while True:
    value = input('Enter the currency you want to convert (q for quit): ').upper()
    if  value == 'Q':
        break
    else:
        weight = input('Enter the amount: ').upper()
        try:
            weight = float(weight)
        except Exception as e:
            print("Wrong amount.")
        data = convert_currency(value)
        del data["data"][value]
        for ticker, value in data['data'].items():
            print(f"{ticker}: {str(float(value)*float(weight))}")