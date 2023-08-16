# Task 1: Createing dictionary

# Create a dictionary with the two lists
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103,101,99,100,100,95,95,96,93,90]

# Print the dictionary  
movie_dict = {years,durations}

for i in range(0, len(years)):
    movie_dict[years[i]] = durations[i]

print(movie_dict)


# Task 2: Creating a DataFrame

# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame (movie_dict, columns=[ "Table" ])

# Print the DataFrame
print(durations_df)


# Task 3:  Creating a line plot