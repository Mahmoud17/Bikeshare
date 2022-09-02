import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to explore the data for chicago, new york city or washington?\n:: ").lower()
    while city not in CITY_DATA:
        city = input("Please chose one of the following: [chicago, new york city, washington]\n:: ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("What month would you like to filter on? [all, january, february, ..., june]\n:: ").lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input("Please enter a valid month name\n:: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What day would you like to filter on? [all, sunday, monday, ..., saturday]\n:: ").lower()
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        day = input("Please enter a valid day name\n:: ").lower()

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    
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

    # TO DO: display the most common month
    print("Busiest month is,", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Busiest day of the week is,", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("Busiest hour is,", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most popular starting station is", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most popular termination station is", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    popular_journey = df[['Start Station', 'End Station']].value_counts().sort_values(ascending=False).reset_index().iloc[0]
    print("Most popular journey is", popular_journey['Start Station'], 'to', popular_journey['End Station'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_seconds = df['Trip Duration'].sum()
    # TO DO: display total travel time
    print(f"Total travel time is {total_seconds // 3600} hours, \
{(total_seconds % 3600) // 60} minutes and {total_seconds % 60} seconds")
    mean_duration = df['Trip Duration'].mean()
    # TO DO: display mean travel time
    print(f"Average travel time is {int(mean_duration // 60)} minutes and\
 {int(mean_duration % 60)} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    if ('Gender' in df.columns) and ('Birth Year' in df.columns): 
        # TO DO: Display counts of gender
        print(df['Gender'].dropna().value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print(f'Earliest year of birth {df["Birth Year"].min()}')
        print(f'Most recent year of birth {df["Birth Year"].max()}')
        print(f'Most common year of birth {df["Birth Year"].mode()}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
