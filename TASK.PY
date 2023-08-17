# Task 1: Createing dictionary

# Create a dictionary with the two lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Print the dictionary
movie_dict = {}
for i in range(0, len(years)):
    movie_dict[years[i]] = durations[i]
print(movie_dict)


# Task 2: Creating a DataFrame

# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict, index=[0])

# Print the DataFrame
print(durations_df)


# Task 3:  Creating a line plot

# Importing matplotlib.pyplot
import matplotlib.pyplot as plt 

# Drawing a line plot of release_years and durations
plt.plot(years,durations)
plt.title ("Netflix Movie Durations 2011-2020")
plt.xlabel("years")
plt.ylabel("durations")
plt.grid(True)
# Show the plot
plt.show()

# Task 4: Loading Data 

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv ("netflix_data.csv")

netflix_df.head(5)

print(netflix_df)

# Task 5:Filtering for Movies
netflix_df_movies_only = netflix_df[netflix_df["type"]=="Movie"]

netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year","duration"]]

netflix_movies_col_subset.head(5)

print(netflix_movies_col_subset)

# Task 6

release_year = netflix_movies_col_subset.get("release_year")
duration = netflix_movies_col_subset.get("duration")

plt.scatter(release_year, duration)
plt.title ("Movie Duration by Year of Release")
plt.xlabel("release_year")
plt.ylabel("duration")
plt.grid(True)
# Show the plot
plt.show()


# Task 7 Digging Deeper
# Filter for durations shorter than 60 minutes

short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"]<60]
short_movies.head(20)
print(short_movies)

# Task 8    
colors = []
genres = netflix_movies_col_subset.get("genre")

for genre in genres:
    if genre == "Children":
      colors.append("red")
    elif genre == "Documentaries":
        colors.append("blue")
    elif genre == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

print([colors[index] for index in range(0, 10)])

# Task 9
plt.scatter(release_year, duration, c=colors)
plt.title ("Movie duration by year of release")
plt.xlabel ( "Release year")
plt.ylabel ( "Duration (min)")
plt.show()