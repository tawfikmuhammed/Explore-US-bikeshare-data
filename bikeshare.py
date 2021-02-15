import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cites=('chicago','new york city','washington')
months=('january','february','march','april ','may','june','all')
days=('saturday','sunday','monday','tuesday','wednesday','thursday', 'friday','all')

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
    while True :
        try:
            number=int(input("Enter city number chicago(1),new york city(2) ,washington(3)             ? \n "))
            if number in (1,2,3):
                city=cites[number-1]
                break
            else :
                print("please enter number from 1 to 3!!")
        except ValueError :
            print("please enter number form 1 to 3 !!")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        try:
            number=int(input("Enter month  number January(1) ,February(2) ,March(3),April(4) ,May(5),June (6) or all(7)? \n  "))
            if number in (1,2,3,4,5,6,7) :
                month=months[number-1]
                break
            else:
                print("please enter number from 1 to 7 !!")
        except ValueError :
            print("please enter number from 1 to 7 !!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        try:
            number=int(input("Enter day number Saturday(1),Sunday(2),monday(3),tuesday(4),wednesday(5),Thursday(6), Friday(7) or all (8) ? \n "))
            if number in (1,2,3,4,5,6,7,8) :
                day=days[number-1]
                break
            else:
                print("please enter number from 1 to 8 !!")
        except ValueError:
            print("please enter number from 1 to 8 !!")

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

    # display the most common month
    common_month=df['month'].mode()[0]
    print("the most common month: {}".format(common_month))
    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print("the most common day of week : {} ".format(common_day))
    # display the most common start hour
    common_hour=df['Start Time'].mode()[0]
    print ("the most common start hour: {}".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print("most commonly used start station: {}".format(common_start))

    # display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print("most commonly used end station: {}".format(common_end))
    # display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+df['End Station']
    common_combination=df['combination'].mode()[0]
    print(" most frequent combination of start station and end station trip : {}".format(common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_tt=df['Trip Duration'].sum()
    print("total travel time : {}".format(total_tt))
    # display mean travel time
    mean_tt=df['Trip Duration'].mean()
    print("mean travel time : {}".format(mean_tt))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types
    type=df['User Type'].value_counts()
    print("Display counts of user types \n {}".format(type))
    # Display counts of gender
    gender=df['Gender'].value_counts()
    print('counts of gender : \n {}'.format(gender))
    # Display earliest, most recent, and most common year of birth
    young_year=df['Birth Year'].max()
    old_year=df['Birth Year'].min()
    most_common=df['Birth Year'].mode()[0]
    print('youngest user : {} \n oldest user : {} \n  most common year of birth : {}'.format(young_year, old_year,most_common))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_row_data(df):
    # view 5 rows
    x=5
    while True:
        data=df.head(x)
        x+=5
        print(data)
        restart = input('\nWould you like to show another data ? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington' :
            user_stats(df)
        display_row_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
