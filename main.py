# Import necessary packages
import pandas as pd
import numpy as np

# Read each file
price = pd.read_csv('data/airbnb_price.csv')
xls = pd.ExcelFile('data/airbnb_room_type.xlsx')
last_review = pd.read_csv('data/airbnb_last_review.tsv', sep = '\t')

# Check what sheets are available

print(xls.sheet_names)

# Parse the xls dataframe to get the columns needed

room_type = xls.parse(0, skiprows=[0], names=['listing_id', 'description', 'room_type'])

# Check data types and possible nulls for price table and an example of the data

price.info()
price.head()

# Strip the str part of the price column then convert it into a float

price['price'] = price['price'].str.strip(' dollars')
price['price'] = price['price'].astype('float')

##What is the average listing price? Round to the nearest two decimal places and save into a variable.

average_price = round(price['price'].mean(),2)

# Check data types and possible nulls for room_type table and an example of the data

room_type.info()

# Change room type column text case into Title and change its data type

room_type['room_type'] = room_type['room_type'].str.title()
room_type['room_type'] = room_type['room_type'].astype('category')

room_type['room_type'].cat.categories

#How many of the listings are private rooms? Save this into any variable.

private_rooms = (room_type['room_type'].values == 'Private Room').sum()

# Check data types and possible nulls for last_review table and an example of the data

last_review.info()
last_review.head()

# Convert last_review column to datetime

last_review['last_review'] = pd.to_datetime(last_review['last_review'])

# What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.

first_reviewed = last_review['last_review'].min()
last_reviewed = last_review['last_review'].max()

# Create dictionary with requested values

review_dates = pd.DataFrame(
    {'first_reviewed': [first_reviewed],
     'last_reviewed': [last_reviewed],
     'nb_private_rooms': [private_rooms],
     'avg_price': [average_price]}
)

print(review_dates)
