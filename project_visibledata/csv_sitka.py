import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    max_t, min_t, ave_t, date_record = [], [], [], []
    for row in reader:
        max_t.append(int(row[1]))
        min_t.append(int(row[3]))
        ave_t.append(int(row[2]))
        date_record.append(datetime.strptime(row[0],"%Y-%m-%d"))


fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(date_record,min_t,c='blue',linewidth=1)
plt.plot(date_record,max_t,c='red',linewidth=1)
plt.plot(date_record,ave_t,c='green',linewidth=1)

plt.ylim([15,75])
plt.ylabel("Temperature (F)",fontsize=16)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()

plt.show()