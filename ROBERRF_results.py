# imports and global vars
import csv
import os
import statistics
import pandas as pd

CINCINNATI = "72429793812"
FLORIDA = "99495199999"
MISSING = ["99.99", "999.9", "9999.9"]

# Remove missing or invalid readings from the dataset in your analysis
# for year in range(2015, 2025):
#     for dataset in os.listdir(str(year)):
#       with open(str(year) + '/' + dataset, "r") as read_file:
#         rows = list(csv.reader(read_file))
#       for r in range(1, len(rows)):
#         rows[r] = [
#           "MISSING" if data in MISSING else data
#           for data in rows[r]
#         ]
#       with open(str(year) + '/' + dataset, "w", newline="") as write_file:
#         writer = csv.writer(write_file)
#         writer.writerows(rows)

# 2. display the count of each dataset
# for year in range(2015, 2025): # loop through years
#   for dataset in os.listdir(str(year)): # loop through files in each year dir
#     with open(str(year) + '/' + dataset, 'r') as file:
#       reader = csv.reader(file)
#       next(reader)
#       row_count = sum(1 for row in reader)
#       if (dataset[:-4] == CINCINNATI):
#         print('{}/Cincinnati - {} rows'.format(year,row_count))
#       else:
#         print('{}/Florida:   - {} rows'.format(year,row_count))

# 3. find the hottest day for each year
# for year in range(2015, 2025): # loop through years
#   maxT = ['', '', '', '-999']
#   for dataset in os.listdir(str(year)): # loop through files in each year dir
#     with open(str(year) + '/' + dataset, 'r') as file:
#       reader = csv.DictReader(file)
#       for i, row in enumerate(reader):
#         if (float(row["MAX"]) > float(maxT[3])):
#           maxT[0] = row["STATION"]
#           maxT[1] = row["NAME"]
#           maxT[2] = row["DATE"]
#           maxT[3] = row["MAX"]
#   print('{} Hottest Day: {}, {}, {}, {}'.format(year, maxT[3], maxT[2], maxT[1], maxT[0]))

# 4. Find the coldest day for the month of March across all years
# minT = ['', '', '', '999.9']
# for year in range(2015, 2025):
#   for dataset in os.listdir(str(year)):
#     with open(str(year) + '/' + dataset, 'r') as file:
#       reader = csv.DictReader(file)
#       for row in reader:
#         if ((row["DATE"][:-3] == "{}-03".format(year)) and 
#             (float(row["MIN"]) < float(minT[3]))):
#           minT[0] = row["STATION"]
#           minT[1] = row["NAME"]
#           minT[2] = row["DATE"]
#           minT[3] = row["MIN"]
# print('OVERALL MIN TEMP: {}, {}, {}, {}'.format(minT[3], minT[2], minT[1], minT[0]))

# 5. Find the year with the most precipitation for Cincinnati and Florida
# cin, fla = ['', '', '', 0.0], ['', '', '', 0.0]
# for year in range(2015, 2025):
#   for dataset in os.listdir(str(year)):
#     with open(str(year) + '/' + dataset, 'r') as file:
#       reader = csv.DictReader(file)
#       prcp_sum, row_count = 0.0, 0.0
#       curr_station, curr_name = '', ''
#       for i, row in enumerate(reader):
#         if (i == 0):
#           curr_station = row["STATION"]
#           curr_name = row["NAME"]
#         prcp_sum += float(row["PRCP"]) 
#         row_count += 1.0
#       prcp_mean = prcp_sum / row_count
#       if (dataset[:-4] == CINCINNATI):
#         if (prcp_mean > cin[3]):
#           cin[0] = curr_station
#           cin[1] = curr_name
#           cin[2] = year
#           cin[3] = prcp_mean
#       else:
#         if (prcp_mean > fla[3]):
#           fla[0] = curr_station
#           fla[1] = curr_name
#           fla[2] = year
#           fla[3] = prcp_mean
# print('Highest PRCP mean Cincinnati: {}, {}, {}, {}'.format(cin[3], cin[2], cin[1], cin[0]))
# print('Highest PRCP mean Florida: {}, {}, {}, {}'.format(fla[3], fla[2], fla[1], fla[0]))

# 6. Count the percentage of missing values for wind gust for Cincinnati and Florida in the year 2024
# for dataset in os.listdir('2024'):
#   with open('2024/' + dataset, 'r') as file:
#     reader = csv.DictReader(file)
#     row_count, missing_count = 0, 0
#     for i, row in enumerate(reader):
#       row_count += 1
#       if (row["GUST"] == "999.9"):
#         missing_count += 1
#     percent_missing = (float(missing_count) / float(row_count)) * 100
#     if (dataset[:-4] == CINCINNATI):
#       print('Missing GUST values Cincinnati 2024 - {}%'.format(percent_missing))
#     else:
#       print('Missing GUST values Florida 2024    - {}%'.format(percent_missing))

# 7. Find the mean, median, mode, and standard deviation of the temperature for Cincinnati 
#    in each month for the year 2020
# months = {
#   1: "January",
#   2: "February",
#   3: "March",
#   4: "April",
#   5: "May",
#   6: "June",
#   7: "July",
#   8: "August",
#   9: "September",
#   10: "October",
#   11: "November",
#   12: "December"
# }
# with open('2020/' + CINCINNATI + '.csv', 'r') as file:
#   reader = csv.DictReader(file)
#   all_temps = [[],[],[],[],[],[],[],[],[],[],[],[]]
#   for row in reader:
#     month = int(row["DATE"][5:7])
#     all_temps[month - 1].append(float(row["TEMP"]))
# for i, data in enumerate(all_temps):
#   mean = statistics.mean(all_temps[i])
#   med = statistics.median(all_temps[i])
#   mode = statistics.mode(all_temps[i])
#   stdev = statistics.stdev(all_temps[i])
#   print('{}\n  ->  mean: {} | median: {} | mode: {} | stdev: {}'.format(months[i+1], mean, med, mode, stdev))

# 8. Find the top 10 days with the lowest Wind Chill for Cincinnati in 2017
# with open('2017/' + CINCINNATI + '.csv', 'r') as file:
#   reader = csv.DictReader(file)
#   WCs = []
#   for row in reader:
#     temp = float(row["TEMP"])
#     windspeed = float(row["WDSP"])
#     wc = 9999.9
#     if ((temp < 50.0) and (windspeed > 3.0)):
#       wc = 35.74 + 0.6215 * temp - 35.75 * (windspeed)**0.16 + 0.4275 * temp * (windspeed)**0.16
#     WCs.append((str(wc), row["DATE"]))
#   data_frame = pd.read_csv('2017/' + CINCINNATI + '.csv')
#   data_frame["WC"] = [wc for wc, _ in WCs]
#   data_frame.to_csv('2017/' + CINCINNATI + '.csv')
#   sorted_wc = sorted(WCs, key=lambda x: float(x[0]))

#   print('10 coldest wind chills in Cincinnati in 2017:')
#   for i in range(10):
#     print('{} -> {}'.format(sorted_wc[i][1], sorted_wc[i][0]))

# # 9. Investigate how many days had extreme weather conditions for Florida using the "FRSHTT" column
# FRSHTT_count = 0
# for year in range(2015, 2025):
#   if (os.path.isfile(str(year) + '/' + str(FLORIDA) + '.csv')):
#     with open(str(year) + '/' + str(FLORIDA) + '.csv', 'r') as file:
#       reader = csv.DictReader(file)
#       for row in reader:
#         if (row["FRSHTT"] != "000000"):
#           FRSHTT_count += 1
# print('Florida days with extreme weather conditions: {}'.format(FRSHTT_count))

# 10. Predict the maximum Temperature for Cincinnati for November and December 2024, 
#     based on the previous 2 years of weather data
# TODO