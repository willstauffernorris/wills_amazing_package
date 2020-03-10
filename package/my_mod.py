
import pandas as pd
'''
test function
'''

def mega(x):
    return x *100

'''
Single function to take a list, turn it into a series and add it to a dataframe as a new column
'''
def list_to_column(x):
    '''
    x must be a list in this format: ['item a', 'item b', 'item c']
    '''
    series = pd.Series(x)
    frame = series.to_frame()
    return frame
