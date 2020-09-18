import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['January', 'February', 'March', 'April', 'May', 'June']
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

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
    while True:
        try:
            city = input('\nwhat city will you like to explore (Chicago, New york city or Washington): ').lower()
            if city == 'chicago' or city == 'new york city' or city == 'washington':
                break
            print('\nenter a valid city!', '\n, chicago, new york city or washington')
        except Exception as e:
            print(e)                         

    # get user input for month (all, january, february, ... , june)
    while True:
        choice = input('\nDo you want to filter by month and/or week? Y/n: ' )    #.lower()
        if choice == 'yes' or choice == 'y':
            choice = True 
        elif choice == 'no' or choice == 'n':
            choice = False
        else:
            print('\nPlease enter a valid choice! ') 
            continue
        break
        
    while True:
        if choice:
            filter = input('\nFilter by month or day or both: ')   #.lower() 
            if filter == 'month':                                 
                #try:
                # month_list = ['January', 'February', 'March', 'April', 'May', 'June']
                day = 'all' 
                month = input('\nMonth to explore(January to June): ').capitalize()
                if month in month_list:
                    print('your chosen month is: ', month) 
                    break
                #print('\ninput a valid month!', '\n, from January to June ')
                else:
                    print('\ninput a valid month!', '\n, Any month from January to June') 
                    
                #except Exception as e:
                    # print(e) 
                # month
                # day = 'all' 
            # get user input for day of week (all, monday, tuesday, ... sunday)
            elif filter == 'day':
                # try:
                # week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                month = 'all' 
                day = input('\nDay of week to explore("all" for all the days): ').capitalize()
                if day in week:
                    print('\nYour chosen day is: ', day) 
                    break                 
                else:
                    print('\ninput a valid day of week and "all" for all the days!')
                # except Exception as e:
                    # print(e)                 
                # month = 'all'                
            elif filter == 'both':
                # try:
                month = input('\nMonth to explore: ').capitalize()
                if month in month_list:
                    print('\nYour chosen month is: ', month) 
                    #continue                
                #print('\ninput a valid month!', '\n, January to June')
                else:
                    print('input a valid month!', '\n, Any month from January to June') 
                # except Exception as e:
                    # print(e) 
                #month = month_list[month]
                # try:
                # week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                print('\n and day of week to explore?') 
                day = input('\nday of week to explore: ').capitalize()
                if day in week:
                    print('your chosen day is: ', day) 
                    break                 
                else:
                    print('input a valid day of week!')
                # except Exception as e:
                    # print(e) 
                # day = week[day]    
            else:
                print('input a valid filter!') 
                continue
            break
        else:
            day = 'All' 
            month = 'All' 
            break
            
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
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    month_list = ['January', 'February', 'March', 'April', 'May', 'June']
    if month in month_list:
        #month_list = ['January', 'February', 'March', 'April', 'May', 'June']
        month = month_list.index(month.capitalize()) + 1
        df = df[df['month'] == month] 
    #week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day != 'all':    #day in week:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = week.index(day.capitalize()) 
        df = df[df['day'] == day] 
        
    df['hour'] = df['Start Time'].dt.hour
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek

    # display the most common month
    commonest_month = df['month'].mode()[0]
    month_list = ['January', 'February', 'March', 'April', 'May', 'June']
    most_freq_month = month_list[commonest_month - 1]
    print('The most common month for bike traveling is {}'.format(most_freq_month))
    	
    # display the most common day of week
    commonest_day = df['day'].mode()[0]
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    most_freq_day = week[commonest_day - 1]
    print('\nThe most common day of the week for bike travel is {}'.format(most_freq_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    commonest_hour = df['hour'].mode()[0]
    print('\nThe most common hour of the day for bike travel is {}'.format(commonest_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonest_start = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is {}.'.format(commonest_start))

    # display most commonly used end station
    commonest_end = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is {}.'.format(commonest_end))

    # display most frequent combination of start station and end station trip
    start_end_combine = 'Start Station: ' + df['Start Station'] + '--->' + 'End Station: ' + df['End Station'] 
    most_freq_combine = start_end_combine.mode()[0]
    print('\nThe most frequent combination of Start Station and End Station trip is {}'.format(most_freq_combine))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['End Time'] = pd.to_datetime(df['End Time']) 
    df['Duration'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])   #df['End Time'] - df['Start Station'] 
    # display total travel time
    total_travel_time = df['Duration'].sum()
    print('\nTotal travel time of trip is {}.'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Duration'].mean()
    print('\nMean travel time of trip is {}.'.format(mean_travel_time)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: {}'.format(user_types))

    # Display counts of gender
    print() 
    if 'Gender' in df.columns:
        print('Counts of gender: {}'.format(df['Gender'].value_counts())) 
    else:
        print('\nOops! Seems gender data is unavailable for {}'.format(city)) 	

    # Display earliest, most recent, and most common year of birth
    print() 
    if 'Birth Year' in df.columns:
        print('\n,Earliest year of birth: {}'.format(int(df['Birth Year'].min()))) 
        print('\n,Most recent year of birth: {}'.format(int(df['Birth Year'].max()))) 
        print('\n,Most common year of birth: {}'.format(int(df['Birth Year'].mode())))
    else:
        print('Oops! Seems Birth Year data is unavailable for {}.'.format(city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df) 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
