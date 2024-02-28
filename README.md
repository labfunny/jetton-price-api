# Python library for working with the TON API to retrieve current token prices.

## Installation

```shell
pip install jettonpriceapi
```
Mainnet:

```python
from jettonpriceapi import *

api = Jettonapi(testnet=False)
```

Testnet:

```python
from jettonpriceapi import *

api = Jettonapi(testnet=True)
```

## Methods

### get_status
Getting the current status of the TON API
Пример:
```python
api.get_status()
```

### get_price
Getting the current token price or TON price
| Parameter | Information |
|---------|-------------|
| tokens | Token or TON |
| currencies | Fiat or TON |

Пример:
```python
price = api.get_price('TON', 'USD')
print(price)
```

### get_diff
Getting the change in token price or TON price
| Parameter | Information |
|---------|-------------|
| tokens | Token or TON |
| diff | 24h, 7d, 30d |
| currencies | Fiat or TON |

Пример:
```python
diff = api.get_diff('TON', '30d', 'USD')
print(diff)
```
