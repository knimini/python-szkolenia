#!/usr/bin/env python3
import datetime
from matplotlib import pyplot as plt
import requests


def date_to_rate(dt, base='JPY', currency='PLN'):
    base_url = 'https://api.fixer.io/{}?base={}&symbols={}'
    date = dt.strftime('%Y-%m-%d')

    url = base_url.format(date, base, currency)
    r = requests.get(url)
    response = r.json()
    return response['rates'][currency]


today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
max_rates = 30

days = list()
rates = list()

for d in range(max_rates):
    date = today - delta * d
    days.append(date)
    currency = 'EUR'
    rates.append(date_to_rate(date, base='USD'))

plt.plot(days[::-1], rates[::-1])
plt.show()
