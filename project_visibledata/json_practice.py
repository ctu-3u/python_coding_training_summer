import os
import json
import pygal
from urllib.request import urlopen


os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('btc_close_2017_urllib.json') as f:
    btc_data = json.load(f)


dates = []
months = []
weeks = []
weekdays = []
closes = []
for btc_datum in btc_data:
    dates.append(btc_datum['date'])
    months.append(int(btc_datum['month']))
    weeks.append(int(btc_datum['week']))
    weekdays.append(btc_datum['weekday'])
    closes.append(float(btc_datum['close']))


fig = pygal.Line(x_label_rotation=90,show_minor_x_labels=False)
fig.title = "Close Prices"
fig.x_labels = dates
fig.x_labels_major = dates[::20]
fig.add("Closes Prices",closes)
fig.render_in_browser()