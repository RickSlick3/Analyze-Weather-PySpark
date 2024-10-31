# imports and global vars
import csv
import os

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