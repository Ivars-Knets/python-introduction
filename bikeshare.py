import time
import pandas as pd

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}
MONTH_NAMES = ['january', 'february', 'march', 'april', 'may', 'june'] #, 'july', 'august', 'september', 'october', 'november', 'december']
DAY_NAMES = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



def validatedInput(message, checkList, allIsValidInput=False):
    """
    An input with validation

    Inputs:
        message (str): message that informs what to input
        checkList (list): list of acceptable inputs
        allIsValidInput (boolean): boolean showing if "all" should be a valid input

    Output:
        (str): the input string

    """
    result = None
    while result == None:
        user_input = input(message)
        if user_input.lower() in checkList or (allIsValidInput and user_input.lower() == 'all'):
            result = user_input.lower()
        else: 
            print('Invalid input. Try again!')

    return result


def validatedIntInput(message, default):
    """
    An input that accepts only integers or empty string (for default value)

    Inputs:
        message (str): message that informs what to input
        default (int): default int value, to use when empty string is input

    Output:
        (int): the input string converted to int
        
    """
    result = None

    while result == None:
        user_input = input(message)        

        if user_input.isdigit():
            result = user_input
        elif user_input == '':
            result = default
        else: 
            print('Invalid input. Try again!')
          
    return int(result)


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
        result = df[[col]]
        if result.empty:
            print(f'No data available for column "{col}"')
            return None
        else: 
            return result
    else:
        print(f'\n--- {col}: no such column available')
        return None


def seconds_to_readable(secs):
    secs_as_int = None

    if isinstance(secs, pd.Series):
        secs_as_int = int(secs.iloc[0])
    else:
        secs_as_int = int(secs)

    secs_in_a_year = 31536000
    full_years = secs_as_int // secs_in_a_year
    remaining_secs_after_years = secs_as_int % secs_in_a_year

    secs_in_a_day = 86400
    full_days = remaining_secs_after_years // secs_in_a_day
    remaining_secs_after_days = secs_as_int % secs_in_a_day

    secs_to_subYear_time = time.strftime('%H hours, %M minutes and %S seconds', time.gmtime(remaining_secs_after_days))

    if full_years > 0:
        return f'{full_years} years, {full_days} days, {secs_to_subYear_time} ({secs_as_int} seconds)'
    elif full_years == 0 and full_days > 0:
        return f'{full_days} days, {secs_to_subYear_time} ({secs_as_int} seconds)'
    else:
        return f'{secs_to_subYear_time} ({secs_as_int} seconds)'



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

    input_city = validatedInput(f'Input a city ({", ".join(CITY_DATA.keys())}): ', CITY_DATA.keys())
    input_month = validatedInput(f'Input name of month (between "{MONTH_NAMES[0]}" and "{MONTH_NAMES[-1]}") ("all" is acceptable): ', MONTH_NAMES, True)
    input_day = validatedInput('Input name of day (eg. "friday") ("all" is acceptable): ', DAY_NAMES, True)


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
    df['Day of Week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        month = MONTH_NAMES.index(month) + 1
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        day_index = DAY_NAMES.index(day)
        df = df[df['Day of Week'] == day_index]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df_start_time = access_df_col(df, 'Start Time')
    if isinstance(df_start_time, pd.DataFrame):
        # display the most common month
        most_common_month = pd.to_datetime(df['Start Time']).dt.month.mode().values[0]
        print(f'The most common month for travel: \n\t{MONTH_NAMES[most_common_month-1]}')


        # display the most common day of week
        most_common_day = pd.to_datetime(df['Start Time']).dt.dayofweek.mode().values[0]
        print(f'The most common day of the week for travel: \n\t{DAY_NAMES[most_common_day]}')


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
    df_start_stations = access_df_col(df, 'Start Station')
    if isinstance(df_start_stations, pd.DataFrame):
        popular_starting_station = df['Start Station'].value_counts().idxmax()
        print(f'The most common starting station: \n\t{popular_starting_station}')


    # display most commonly used end station
    df_end_stations = access_df_col(df, 'End Station')
    if isinstance(df_end_stations, pd.DataFrame):
        popular_ending_station = df['End Station'].value_counts().idxmax()
        print(f'The most common ending station: \n\t{popular_ending_station}')


    # display most frequent combination of start station and end station trip
    if isinstance(df_start_stations, pd.DataFrame) and isinstance(df_end_stations, pd.DataFrame):
        most_common_station_combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print(f'The most common combination of starting and ending stations:')
        print(f'\tStarting station: {most_common_station_combo[0]}')
        print(f'\tEnding station: {most_common_station_combo[1]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    df_trip_duration = access_df_col(df, 'Trip Duration')
    if isinstance(df_trip_duration, pd.DataFrame):

        # display total travel time
        total_travel_time = df_trip_duration.sum()
        print(f'Total travel time: \n\t{seconds_to_readable(total_travel_time)}')

        # display mean travel time
        mean_travel_time = df_trip_duration.mean()
        print(f'Mean travel time: \n\t{seconds_to_readable(mean_travel_time)}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df_user_types = access_df_col(df, 'User Type')
    if isinstance(df_user_types, pd.DataFrame):
        user_type_count = df['User Type'].value_counts(dropna= False).to_string(header= False)
        print(f'\nCount of users per type: \n{user_type_count}')


    # Display counts of gender
    df_user_genders = access_df_col(df, 'Gender')
    if isinstance(df_user_genders, pd.DataFrame):
        user_gender_count = df['Gender'].value_counts(dropna= False).to_string(header= False)
        print(f'\nCount of users per gender: \n{user_gender_count}')


    # Display earliest, most recent, and most common year of birth
    df_user_birth_years = access_df_col(df, 'Birth Year')
    if isinstance(df_user_birth_years, pd.DataFrame):
        print('\nBirth year:')
        print(f'Earliest: {df_user_birth_years.min().values[0].astype(int)}')
        print(f'Latest: {df_user_birth_years.max().values[0].astype(int)}')
        print(f'Most common: {df_user_birth_years.mode().values[0][0].astype(int)}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    """ Asks if users wants to see a set amount of lines of raw data. And keeps repeating the question until user does not say 'yes' or all the data has been shown. """
    df_len = len(df.index)
    step = 5
    start_line = 0

    show = validatedInput(f'Would you like to see a set lines from the raw data? (yes/no, y/n) : ', ['yes', 'no', 'y', 'n', ''])

    while show.lower() in ['yes', 'y']:
        step = validatedIntInput('How many lines would you like to see (press Enter for default of 5): ', 5)
        end_line = start_line + step

        if end_line >= df_len:            
            print(df.iloc[start_line : (df_len)].to_string())
            print('\n\nEnd of Data!')
            break
        else:
            print(df.iloc[start_line : end_line].to_string())
            start_line = end_line
            show = validatedInput(f'Would you like to see another set of {step} lines of data? (yes/no, y/n) : ', ['yes', 'no', 'y', 'n', ''])


    start_line = 0
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if not df.empty:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            show_raw_data(df)
        else:
            print('No data available!')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
