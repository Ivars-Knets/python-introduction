import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_names = ['january', 'february', 'march', 'april', 'may', 'june'] #, 'july', 'august', 'september', 'october', 'november', 'december'
day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def access_df_col(df, col):
    """
    Checks that the column that will be accessed is in the DataFrame

    Input:
        (pd.DataFrame): df - the DataFrame
        (str) col - the column that will be accessed

    Returns:
        (pd.Series/None): accessed column data as a pd.Series
    """
    if col in df.columns:
        return df[[col]]
    else:
        print(f'\n--- {col}: no such column available')
        return None



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    def validatedInput(text, checkList):
        result = None
        while result == None:
            user_input = input(text)
            if user_input.lower() in checkList:
                result = user_input.lower()
            else: 
                print('Invalid input. Try again!')
        return result


    input_city = validatedInput('Input a city (chicago, new york city, washington): ', CITY_DATA.keys())
    input_month = validatedInput('Input month name (between "january" and "june"): ', month_names)
    input_day = validatedInput('Input day name (eg. "friday"): ', day_names)


    print('-'*40)
    return input_city, input_month, input_day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    path = f'data/{CITY_DATA[city]}'
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = pd.to_datetime(df['Start Time']).dt.month.mode().values[0]
    print(f'The most common month for travel: \n\t{month_names[most_common_month-1]}')


    # display the most common day of week
    most_common_day = pd.to_datetime(df['Start Time']).dt.day_of_week.mode().values[0]
    print(f'The most common day of the week for travel: \n\t{day_names[most_common_day]}')


    # display the most common start hour
    most_common_hour = pd.to_datetime(df['Start Time']).dt.hour.mode().values[0]
    print(f'The most common start hour for travel: \n\t{most_common_hour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_startStation = df['Start Station'].value_counts().idxmax()
    print(f'The most common starting station: \n\t{most_common_startStation}')


    # display most commonly used end station
    most_common_endStation = df['End Station'].value_counts().idxmax()
    print(f'The most common ending station: \n\t{most_common_endStation}')


    # display most frequent combination of start station and end station trip
    most_common_station_combo = df[['Start Station', 'End Station']].value_counts().idxmax()
    print(f'The most common combination of starting and ending stations:')
    print(f'\tStarting station: {most_common_station_combo[0]}')
    print(f'\tEnding station: {most_common_station_combo[1]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Travel Time'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # display total travel time
    total_travel_time = df['Travel Time'].sum()
    print(f'Total travel time: \n\t{total_travel_time}')

    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print(f'Mean travel time: \n\t{mean_travel_time}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_per_type = access_df_col(df, 'User Type')
    if isinstance(user_per_type, pd.DataFrame):
        print(f'\nCount of users per type: \n{user_per_type.value_counts(dropna= False).to_string(header= False)}')


    # Display counts of gender
    user_per_gender = access_df_col(df, 'Gender')
    if isinstance(user_per_gender, pd.DataFrame):
        print(f'\nCount of users per gender: \n{user_per_gender.value_counts(dropna= False).to_string(header= False)}')


    # Display earliest, most recent, and most common year of birth
    user_birth_years = access_df_col(df, 'Birth Year')
    if isinstance(user_birth_years, pd.DataFrame):
        print('\nBirth year:')
        print(f'Earliest: {user_birth_years.min().values[0].astype(int)}')
        print(f'Latest: {user_birth_years.max().values[0].astype(int)}')
        print(f'Most common: {user_birth_years.mode().values[0][0].astype(int)}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    """ Asks if users wants to see a set amount of lines of raw data. And keeps repeating the question untill user does not say 'yes' or all the data has been shown. """
    df_len = len(df.index)
    step = 5
    start_line = 14334

    show = input(f'Would you like to see {step} lines of the raw data? Enter yes or no. : ')
    while show.lower() == 'yes':
        end_line = start_line + step

        if end_line >= df_len:            
            print(df.iloc[start_line : (df_len)].to_string())
            print('\n\nEnd of Data!')
            break
        else:
            print(df.iloc[start_line : end_line].to_string())
            start_line = end_line
            show = input(f'Would you like to see another set of {step} lines of data? Enter yes or no. : ')


    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
