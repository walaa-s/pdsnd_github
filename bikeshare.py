import time
import pandas as pd
import numpy as np
  
  print("Hello WALAA")

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    #input the search data by user and limiting it to the current options
    while True:
        city = input("please choose the city:  \nfor 'chicago' enter '1', 'new york city' enter '2', 'washington' enter '3': ").lower()
        if city in CITY_DATA:
            break
        else:
            print('enter a right city name')

    #limiting the input to the current options
    while True:
        month= input("select a month from the following:\n 'january', 'february', 'march', 'april', 'may', 'june' or 'all'. :" ).lower()
        if month in (['january', 'february', 'march', 'april', 'may', 'june','all']):
            break
        else:
            print("invalid input please enter valid")

    #limiting the input to the current options
    while True:
        day= input("choose day:('sunday','monday','thuesday','wednesday','thursday','friday','saturday','all'): ").lower()
        if day in (['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']):
            break
        else:
            print("invalid input please enter valid")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    #reading the data from the chosen file by user
    df = pd.read_csv(CITY_DATA[city])

    #converting the srart time into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #month
    df['month'] = df['Start Time'].dt.month
    #week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #hour
    df['hour'] = df['Start Time'].dt.hour

    #incase the user choose a month not all:
    if month != 'all':
        #if filtering by month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        #filtering by selected day_of_week
        theDay = df[df['day_of_week'] == day.title()]
        return theDay
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #calculating the most_common_month
    #mode() shows the most repeated number of the list, and [0] to pick only the value not the index in the df,series
    most_common_month = df['month'].mode()[0]
    print('the most common month is:', most_common_month)

    #calculating the most_common_day
    most_common_day= df['day_of_week'].mode()[0]
    print('most common day of the week is: ', most_common_day)

    #calculating the most_common_start_hour
    most_common_start_hour = df['hour'].mode()[0]
    print('And the most common start hour is:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #displaying the most common start station
    start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', start_station)

    # displaying the most common end station
    end_station = df['End Station'].mode()[0]
    print('The most common End station is: ', end_station)

    #displaying the most common end station
    most_common_grouped_stations =df.groupby(['Start Station','End Station']).size().sort_values().tail(1)
    print('The most common start and end station in the city is: ',most_common_grouped_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #displaying the total travel times
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is:', total_travel_time)

    # display mean travel time
    mean_of_travel_time = df['Trip Duration'].mean()
    print('The mean of the travel time is: ', mean_of_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_type = df['User Type'].value_counts().to_frame()
    print('The count of User type is:\n', count_of_user_type)

    #  Display counts of gender

    try:
        gender_count= df['Gender'].value_counts().to_frame()
        print('The data sorted by gender: \n', gender_count)

        earliest_DOB_year=int( df['Birth Year'].min())
        recent_DOB_year = int(df['Birth Year'].max())
        common_DOB_year= int(df['Birth Year'].mode()[0])

        print('The earliest year of birth : \n', earliest_DOB_year)
        print('The most recent year of birth : \n', recent_DOB_year)
        print('The most common year of birth : \n', common_DOB_year)

    except:
        print('sorry this data is not available in Washington')
        print('No Birth Year Data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(city):
    ##print('Now after you determind the City, Month, Day...')
    answer = str(input("would you like display 5 row data? Enter Y/N : ")).lower()
    while answer not in ('y', 'n'):
        print("please type 'Y' or 'N': ")
    index = 5
    while answer == 'y':
        try:
            for i in pd.read_csv(CITY_DATA[city],  chunksize= index):
                print(i)
                break
            question2 = input('would you like display 5 row data? Enter Y/N :').lower()
            if question2 == 'y':

                index +=5
                continue
            else:
                print('Thank You')
                break
            break

        except:
            print('thanks')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(city)


        restart = input('\nWould you like to restart? Enter Y/N : ')
        if restart.lower() != 'y':
            def printIno():
                print("Thank you ..")
                print("Good job")
            break

if __name__ == "__main__":
    main()
