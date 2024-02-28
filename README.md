# SDK для работы с TON API для получения текущей цены токенов

## Установка

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

## Методы

### get_status
Стостояние TON API
Пример:
```python
api.get_status()
```

### get_price
| Параметр | Информация |
|---------|-------------|
| tokens | Токен или же TON |
| currencies | Фиат или же TON |

Пример:
```python
price = api.get_price('TON', 'USD')
print(price)
```

### get_diff
| Параметр | Информация |
|---------|-------------|
| tokens | Токен или же TON |
| diff | 24h 7d 30d |
| currencies | Фиат или же TON |

Пример:
```python
diff = api.get_diff('TON', '30d', 'USD')
print(diff)
```
