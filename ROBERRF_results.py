# imports and global vars
import csv
import os

CINCINNATI = '72429793812'
FLORIDA = '99495199999'

# Remove missing or invalid readings from the dataset in your analysis
# TODO

# 2. display the count of each dataset
for year in range(2015, 2025): # loop through years
  for dataset in os.listdir(str(year)): # loop through files in each year dir
    with open(str(year) + '/' + dataset, 'r') as file:
      reader = csv.reader(file)
      next(reader)
      row_count = sum(1 for row in reader)
      if (dataset[:-4] == CINCINNATI):
        print('{}/Cincinnati - {} rows'.format(year,row_count))
      else:
        print('{}/Florida:   - {} rows'.format(year,row_count))

# 3. find the hottest day for each year
for year in range(2015, 2025): # loop through years
  maxT = ['', '', '', '-999']
  for dataset in os.listdir(str(year)): # loop through files in each year dir
    with open(str(year) + '/' + dataset, 'r') as file:
      reader = csv.DictReader(file)
      for i, row in enumerate(reader):
        if (float(row["MAX"]) > float(maxT[3])):
          maxT[0] = row["STATION"]
          maxT[1] = row["NAME"]
          maxT[2] = row["DATE"]
          maxT[3] = row["MAX"]
  print('{} MAX TEMP: {}, {}, {}, {}'.format(year, maxT[0], maxT[1], maxT[2], maxT[3]))