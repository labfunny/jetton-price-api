from jettonpriceapi import *

api = Jettonapi(testnet=True)

status = api.get_status()
price = api.get_price('TON', 'USD')
diff = api.get_diff('TON', '30d', 'USD')

print(status)
print(price)
print(diff)
