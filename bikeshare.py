# syvv
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
months = ['all','january','february','march','april','may','june']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
    while True:
        city = input('Please input the name of city (chicago, new york city, washington):').lower()
        if city in cities:
            break
        else:
            print('Not in 3 city on dataset, please try again')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please input the month (january, february, etc):').lower()
        if month in months:
            break
        else:
            print('Not in valid, please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input the day (monday, tuesday, etc):').lower()
        if day in days:
            break
        else:
            print('Not in valid, please try again')

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
    #load data
    df = pd.read_csv('{}.csv'.format(city))
    
    #convert datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #extract month & day
    df['month'] = df['Start Time'].dt.month
    df['dow'] = df['Start Time'].dt.weekday_name
    
    #filter date
    if month != 'all':
        months = ['january','february','march','april','may','june'] 
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['dow'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel.\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is ', df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print('The most common day of week is ', df['dow'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common hour is ', df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip.\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common used start station is ', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('The most common used end station is ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    most_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip : \n {}'.format(most_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration.\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum() / 3600
    print('Total time to travel: {} hour'.format(total.round(2)))
    
    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean() / 3600
    print('Mean time to travel: {} hour'.format(mean.round(2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats.\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Count by user type:\n', user_type)

    # TO DO: Display counts of gender
    try:   
        user_gender = df['Gender'].value_counts()
        print('\nCount by gender:\n', user_gender)
    except:
        print('\nCount by gender: no gender data not available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_bd = df['Birth Year'].min()
        most_recent_bd = df['Birth Year'].max()
        most_common_bd = df['Birth Year'].value_counts().idxmax()
        print('\nEarliest of birthday {}, most recent of birthday {} and most common of birthday {}'.format(int(earliest_bd), int(most_recent_bd), int(most_common_bd)))
    except:
        print('\nAnalysis for birthday: not available data for this city')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def preview_data(df):
    """Show 5 row on data review."""
    start = 0
    end = 5
    df_lengh = len(df.index)
    
    while start < df_lengh:
        ques = input('\nWhat would you see preview data (yes/no)? \n')
        if ques.lower() == 'yes':
            print('\n5 row on data set:\n')
            if end > df_lengh:
                end = df_lengh
            print(df.iloc[start:end])
            start += 5
            end += 5
        else:
            break
           
def main():
    """The main function of project."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        preview_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
