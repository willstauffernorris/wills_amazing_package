
from package.my_mod import Roadtrip
from package.my_mod import date_breaker
from package.my_mod import list_to_series
import pandas as pd

from package.my_mod import mega

print('hell ya')


i = 5
print("number", i)

print("mega number", mega(i))


wills_list = [1, 2, 3]
print('before')
print(type(wills_list))
wills_list = list_to_series(wills_list)
print('after')
print(type(wills_list))

data = {'date': [20200310, 20200309, 20200308]}
df = pd.DataFrame(data=data)
print(df)
print(df['date'])

print(type(df['date'][0]))

date_breaker(df, 'date')
print(df)


trip = Roadtrip("ski trip", "San Francisco")
trip.add_stop("Reno", 425)
trip.add_stop("Boise", 630)
trip.add_stop("Sun Valley", 200)
print(trip.distance)
print(trip.stops)
print(trip.origin)
print(trip.destination)
print(trip)
