import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
#Cities with gender and brth_yr data
cities_gender_birth = ['chicago', 'new york city']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nYou will be asked to provide three inputs for this analysis:\n')
    print('1)The name of the city to analyze.')
    print('  There are 3 choices available for cities to analyze: chicago, new york city, and washington.\n')
    print('2)The name of the month to filter by.')
    print('  There are 7 options available for month to filter: all, january, february, ... , june.\n')
    print('3)The name of the day of the week to filter by.')
    print('  There are 8 options available for this filter: all, monday, tuesday, ... , sunday.\n')

    print('-'*40)


    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in CITY_DATA:
        city = str(input('Enter the name of the city you would like to analyze: ')).lower()
        if city in CITY_DATA:
            break
        else:
            print('That\'s not a valid city name!')
            print('Valid city names are: chicago, new york city, and washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in months:
        month = str(input('Enter the name of the month to filter by, or \"all\" to apply no month filter: ')).lower()
        if month in months:
            break
        else:
             print('That\'s not a valid month name!\n')
             print('Valid options for month filter are: january, february, march, april, may, june, and all.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ""
    while day not in weekdays:
        day = str(input('Enter the name of the day of week to filter by, or "all" to apply no day filter: ')).lower()
        if day in weekdays:
            break
        else:
            print('That\'s not a valid day name!')
            print('Valid options for day filter are: monday, tuesday, wednesday, thursday, friday, saturday, sunday, and all.')
    print('-'*40)
    return city, month, day


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO 1: display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', months[common_month-1].title())

    # TO DO 2: display the most common day of week
    # extract day from the Start Time column to create a month column
    df['day'] = df['Start Time'].dt.weekday
    # find the most common day of the week
    common_day = df['day'].mode()[0]
    print('Most Common Day of Week:', weekdays[common_day].title())

    # TO DO 3: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO 4: display most commonly used start station
    # find the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost Commonly Used Start Station:', common_start_station)

    # TO DO 5: display most commonly used end station
    # find the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # TO DO 6: display most frequent combination of start station and end station trip
    # Create a combination for Start and End Stations
    df['AND'] = " AND "
    df['Start and End Station'] = df['Start Station'] + df['AND'] + df['End Station']
    common_start_end_station = df['Start and End Station'].mode()[0]
    print('Most Commonly Used Combination of Start and End Station:', common_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO 7: display total travel time
    print('Total travel time: ', int(df['Trip Duration'].sum()), 'seconds')

    # TO DO 8: display mean travel time
    print('Mean travel time: ', int(df['Trip Duration'].mean()), 'seconds')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    city = ""
    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO 9: Display counts of user types
    print('\nCounts of user types:\n',df['User Type'].value_counts())

    # TO DO 10: Display counts of gender
    if 'Gender' in df:
        print('\nCounts of genders:\n',df['Gender'].value_counts())
    else:
        print('\nThere is no gender data for Washington')
    # TO DO 11: Display earliest, most recent, and most common year of birth
    if 'brth_yr' in df:
        print('\nEarliest year of birth:', int(df['brth_yr'].min()))
        print('Most recent year of birth:', int(df['brth_yr'].max()))
        print('Most common year of birth:', int(df['brth_yr'].mode()))
    else:
        print('\nThere is no birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def display_data(df):
    """Displays the raw data. First, asks whether the user want to see the raw data.
       If the user says "Yes", then it displays the first 5 rows of the data. Then,
       it asks whether the user would like to see 5 more lines of the raw data. If
       the user says "Yes", then it displays the next 5 rows of the data. The same
       question is asked, until the user says "No"."""
    first = 0
    last = first + 5
    answer = str(input('Would you like to see the raw data (yes/no)?')).lower()
    if answer == "yes":
        displaying = df[first:last]
        print('Displaying the first 5 lines of the raw data:\n', '-'*40, displaying)

    while answer != "no":
        answer = str(input('Would you like to see the next 5 line of the raw data (yes/no)?')).lower()
        if answer == "no":
            break
        else:
            first+=5
            last+=5
            displaying = df[first:last]
            print('Displaying the next 5 lines  of the raw data between row = {} and row = {}:\n'.format(first, last))
            print('-'*40, displaying)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(load_data(city, month, day))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
