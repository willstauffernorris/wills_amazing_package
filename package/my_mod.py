
import pandas as pd
'''
test function
'''


def mega(i):
    return i * 100


'''
Single function to take a list, turn it into a series
'''


def list_to_series(y):
    '''
    x must be a list in this format: ['item a', 'item b', 'item c']
    '''
    series = pd.Series(y)
    print(series)


def date_breaker(df, x):
    '''
    This function breaks a date column into 'year', 'month', 'day', and 'day of year' columns
    x must be a dataframe column
    for example, it might look like: "df['Date']".

    The format must be year/month/day
    '''

    df[x] = pd.to_datetime(df[x], format='%Y%m%d')

    df['Year'] = df[x].dt.year
    df['Month'] = df[x].dt.month
    df['Day'] = df[x].dt.day
    df['Day_of_year'] = ((df['Month'] * 30.333 - 30).round(0) + df['Day'])


class Roadtrip():
    def __init__(self, name, origin):
        self.stops = [origin]
        self.distance = 0
        self.name = name

    def __str__(self):
        return(f"This is a roadtrip from {self.origin} to {self.destination}")

    def __repr__(self):
        return(f"This is a roadtrip from {self.origin} to {self.destination}")

    @property
    def origin(self):
        return self.stops[0]

    @property
    def destination(self):
        return self.stops[-1]

    def add_stop(self, newstop, add_distance):
        self.distance = self.distance + add_distance
        self.stops.append(newstop)
