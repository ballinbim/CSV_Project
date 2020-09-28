import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

# print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

lows = []
highs = []
dates = []

# x = datetime.strptime('2018-07-01','%Y-%m-%d')
# print(x)


for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d') #strip out time
    except ValueError:
        print("Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter = ",")

header_row = next(csv_file2)

# print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

lows2 = []
highs2 = []
dates2 = []

# x = datetime.strptime('2018-07-01','%Y-%m-%d')
# print(x)


for row in csv_file2:
    highs2.append(int(row[5]))
    lows2.append(int(row[6]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates2.append(the_date)

# print(highs)


# print(highs)

import matplotlib.pyplot as plt


fig, ax = plt.subplots(2,1)  #  this will create a visualization with 2 charts on it

ax[0].plot(dates2, highs2, c = "red", alpha = 0.5) #row=0, col=0
ax[0].plot(dates2, lows2, c = "blue", alpha = 0.5) #row=1, col=0
ax[0].fill_between(dates2, highs2, lows2, facecolor = 'blue', alpha = 0.1)
ax[0].set_title("Sitka Airport, AK")
ax[0].set_ylabel("Temperature (F)", fontsize = 8)
ax[0].tick_params(axis = "both", labelsize = 10)

fig.suptitle("Temperature comparison between Sitka Airport, AK and Death Valley, CA")

#Change the appearance of the ticks, tick labels, and gridlines
# fig.tick_params(axis = "both", labelsize = 8)

ax[1].plot(dates, highs, c = "red", alpha = 0.5) #row=0, col=0
ax[1].plot(dates, lows, c = "blue", alpha = 0.5) #row=1, col=0
ax[1].fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
ax[1].set_title("Death Valley, CA")
ax[1].set_ylabel("Temperature (F)", fontsize = 8)
ax[1].tick_params(axis = "both", labelsize = 10)

#The call to fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
fig.autofmt_xdate()

plt.show()




