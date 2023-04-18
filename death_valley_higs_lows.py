from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt
from Temperature_Index_Extractor import Temperature_Index_Extractor as TIE



path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader =  csv.reader(lines)
header_row = next(reader)

max_Temperature_Index = TIE(header_row).get_max_temperature_index()
min_Temperature_Index = TIE(header_row).get_min_temperature_index()

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[max_Temperature_Index])
        low = int(row[min_Temperature_Index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#plot the high temperatures.

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha =0.5)
ax.plot(dates, lows, color='blue', alpha =0.5)
ax.fill_between(dates, highs, lows, facecolor='white', alpha=0.1)

#formating plot

ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=24)
ax.set_xlabel('', fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()