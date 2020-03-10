
import pandas as pd
'''
test function
'''

def mega(x):
    return x *100

'''
Single function to take a list, turn it into a series
'''
def list_to_series(x):
    '''
    x must be a list in this format: ['item a', 'item b', 'item c']
    '''
    series = pd.Series(x)
    print(series)
