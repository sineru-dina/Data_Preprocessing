import datetime
import argparse

import dataload
import date_coding
import visualize

parser = argparse.ArgumentParser(description='Date Encoding & Decoding')

parser.add_argument('--data_path', type=str, default='/data/price_data.csv', help='Path to the price data file')

args = parser.parse_args()

## Load daily price data
data = dataload.data_load(args.data_path)

# Define the years you're interested in
years = [i for i in range(2002, 2022)]

list_d = []
list_y = []

# Loop through the years
for year in years:
    pv_data = data.loc[data['date'].dt.year.isin([year-1, year, year+1])]
    pv_idx = pv_data.loc[pv_data['date'].dt.year == year].index
    
    for idx in pv_idx:
        list_d.append(date_coding.encode_date(pv_data.loc[idx, 'date']))
        list_y.append(year)

print(len(list_d))
print(len(list_y))
print(list_d[:5])
print(list_y[:5])

visualize.plot_encoded_dates(list_d)

# count_2002 = list_y.count(2002)
# print(count_2002)
# visualize.plot_encoded_dates(list_d[:count_2002])

# decoding all the dates
list_deco = [date_coding.decode_date(d, y) for d, y in zip(list_d, list_y)]

# convert to datetime
list_deco = [datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d') for date in list_deco]

print(len(list_deco))
print(list_deco[:5])
