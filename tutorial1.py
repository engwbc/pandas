import pandas as pd
import re
import numpy as np
#Importing data
df = pd.read_csv('pokemon_data.txt', delimiter = '\t') #Delimiter to create tabs between columns to separate them.
print(df.head(5))
#Reading data in pandas

#Reading headers
print(df.columns)
#Read each column
print(df['Name'][0:11]) #[0:11] lists first 11 pokemans
print(df[['Name', 'Type 1', 'HP']]) #Print out Name, type 1 and hp of pokemon
#Read each row
print(df.iloc[0:4]) #iloc = integer location.  Can input a range to index multiple rows.
#Read a specific location (R,C)
print(df.iloc[0,1]) #Returns Pokemon name (row 0, column 1 = Name)

#Iterating through rows
"""for index, row in df.iterrows():
    print(index, row['Name'])"""

#Finding specific data that isn't just rows or columns
print(df.loc[df['Type 1'] == 'Fire']) #Returns fire type pokeman

print(f'\nDescriptive statistics:\n {df.describe()}')

#Sorting
#df.sort_values('Name', ascending = False)
#df.sort_values(['Type 1','HP']) #Descending Type and ascending HP

#Making changes to the data
"""df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))"""

#Filtering data
"""This filters pokemon that are grass and poison type, having HP > 50.
Note parentheses between each parameter"""
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 50)] 
print(new_df)
"""Removing Pokemon containing 'Mega' in their name. Note the use of '~' to denote 'Not'."""
print(df.loc[~df['Name'].str.contains('Mega')])
"""Going a step further with Regex notations. Make sure to import regex"""
#Indexes Fire and Grass type pokeman. #regex = True to enable regex 
print(df.loc[df['Type 1'].str.contains('Fire|Grass', flags = re.I,regex = True)]) #Use flags = re.I to ignore capatilisation
#Index pokemon containing pi in their names
print(df.loc[df['Name'].str.contains('pi', flags = re.I,regex = True)])
#Index for pokemon with names STARTING with pi
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I,regex = True)]) #Regex notation '^' means start

#Conditional changes to the dataframe
#Changes Type 1 data, fire to blazer 
mod_fire = df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Blaze'
#Change all fire pokeman to legendary
leg_fire = df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
#Modifying multiple columns by passing in a list
conditions = [
(df['Attack'] >= 100),
(df['Defense'] >= 90) | (df['HP'] >= 80),
(df['Attack'] <= df['Defense']) | (df['HP'] <= df['Defense'])
]
pokemon_class = ['DPS','Tank','Balanced']
df['Class'] = np.select(conditions,pokemon_class)
print(df)