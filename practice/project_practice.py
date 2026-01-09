import time
import pandas as pd
import numpy as np


## Task 0
## use pandas to answer the questions

chicago_df = pd.read_csv('project/chicago.csv')

## What columns are in this dataset?
# print('\n Columns?\n')
# print(chicago_df.columns)

## Are there any missing values?
# print('\n\n Are there any missing values?\n')
# print(chicago_df.isnull().any())

## What are the different types of values in each column?
# print('\n\n Value types per column? \n')
# print(chicago_df.dtypes)



## Task #1 - Compute the Most Popular Start Hour (using chicago.csv)

def getPopularStartingHours(data_frame):
    hours = pd.to_datetime(data_frame['Start Time']).dt.hour
    return hours.mode().values[0]
    
print("\nMost popular starting hour in Chicago is: ", getPopularStartingHours(chicago_df))



## Task #2 - Display a Breakdown of User Types
def userTypeBreakdown(data_frame):
    return data_frame['User Type'].value_counts()

user_types = userTypeBreakdown(chicago_df)
print("\nUser type breakdown for Chicago: ", user_types)



## Task #3 - Load and Filter the Dataset
## 1 - Load the dataset for the specified city. Index the global CITY_DATA dictionary object to get the corresponding filename for the given city name.
## 2 - Create month and day_of_week columns. Convert the "Start Time" column to datetime and extract the month number and weekday name into separate columns using the datetime module.
## 3 - Filter by month. Since the month parameter is given as the name of the month, you'll need to first convert this to the corresponding month number. Then, select rows of the dataframe that have the specified month and reassign this as the new dataframe.
## 4 - Filter by day of week. Select rows of the dataframe that have the specified day of week and reassign this as the new dataframe. (Note: Capitalize the day parameter with the title() method to match the title case used in the day_of_week column!)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    path = f'project/{CITY_DATA[city]}'
    df = pd.read_csv(path)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_of_week

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = day_names.index(day)
        df = df[df['Day of Week'] == day_index]
    
    return df
    

filtered_data = load_data('chicago', 'march', 'friday')

print("\n\n")
print(filtered_data.head())