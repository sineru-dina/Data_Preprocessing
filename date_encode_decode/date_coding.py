import numpy as np
import datetime

def encode_date(date):
    day_of_year = date.timetuple().tm_yday
    sine = np.sin(2 * np.pi * day_of_year / 365.0)
    cosine = np.cos(2 * np.pi * day_of_year / 365.0)
    return np.array([sine, cosine])

def decode_date(encoded, year):
    sine, cosine = encoded
    day_of_year = np.arctan2(sine, cosine) * (365.0 / (2 * np.pi))

    if day_of_year < 0:
        day_of_year += 365.0

    day_of_year = int(round(day_of_year))

    if day_of_year == 0:
        day_of_year = 365

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap and day_of_year > 365:
        day_of_year = 1

    date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=day_of_year - 1)

    return date