import pandas

print('is this working')

class DataProcessor():
    def __init__(self, my_df):
        self.df = my_df

    def add_state_names(my_df):
        """
        Add a column of state names to a dataframe that already has the abbrevs
        Param my_df pandas.DataFrame should have a column of "abbrev"
        Return a copy of the DataFrame with a new column called "name"
        """
        names_map = {'CT': 'connecticut', 'CO': 'colorado', 'CA': 'california'}
        new_df = my_df.copy()
        new_df['name']=my_df['abbrev'].map(names_map)
        #breakpoint()
        return new_df

df1 = pandas.DataFrame({'abbrev': ['CT', 'CO', 'CA']})

df2 = pandas.DataFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})

for df in [df1, df2]:
    processor = DataProcessor(df)
    processor.add_state_names()
    print(my_frame.head())


'''
mutated_df = add_state_names(df)
print(mutated_df.head())



mutated_df2 = add_state_names(df2)
print(mutated_df2.head())
'''