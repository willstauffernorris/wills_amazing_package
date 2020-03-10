'''
test function
'''


def mega(x):
    return x *100



##------------------
###Make a "Date" splitter

### x must be a 'date' column in a dataframe

'''
def date_splitter(x):
    df[x] = pd.to_datetime(df['Date'], format='%Y%m%d')
    df['Year'] = df['Date'].dt.year
    df['Month']= df['Date'].dt.month
    df['Day']= df['Date'].dt.day
    df['Day_of_year'] = ((df['Month']*30.333-30).round(0) + df['Day'])

x = input()
'''