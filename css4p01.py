# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:27:40 2024

@author: Joshua van Zyl
"""

""" IMPORTING OF LIBRARIES """

import pandas as pd

from ydata_profiling import ProfileReport as PR

# import numpy as np

# import matplotlib.pyplot as plt


""" LOADING OF DATA """

movie_df = pd.read_csv("movie_dataset.csv")

movie_df.drop(["Rank"], inplace=True, axis=1)

col_names = ["Title", "Genre", "Description", "Director", "Actors", "Year", "Runtime_minutes", "Rating", "Votes", "Revenue_millions", "Metascore"]

movie_df.columns = col_names

""" CLEANING UP OF DATA """

# Replace NAN Revenue with the mean of revenue, to not influince the other data.
revenue_mean = round(movie_df["Revenue_millions"].mean(), 2)
movie_df["Revenue_millions"].fillna(revenue_mean, inplace = True)

# Replace NAN Metascore with the mean of metascore, to not influince the other data.
metascore_mean = round(movie_df["Metascore"].mean(), 0)
movie_df["Metascore"].fillna(metascore_mean, inplace = True)


""" Question 1 """

print("Question 1: What is the highest rated movie?")

# get index of highest rated movie
highest_rated_index = movie_df["Rating"].idxmax()   
# get Title of highest rated index
highest_rated_movie = movie_df.loc[highest_rated_index, "Title"]

print("Answer 1: The highest rated movie is:",highest_rated_movie,"\n")


""" Question 2 """

print("Question 2: What is the average revenue of all movies in the dataset?")

# calculate the mean value of the revenue column and round to two decimals
average_revenue = round(movie_df["Revenue_millions"].mean(), 2)

print("Answer 2: The average revenue of all movies in the dataset is: $",average_revenue,"million\n")


""" Question 3 """

print("Question 3: What is the average revenue of movies from 2015 to 2017 in the dataset?")

# filter movies to exclude before 2015
movie_15to17 = movie_df[movie_df['Year'] >= 2015]
# calculate mean value as before
average_revenue_15to17 = round(movie_15to17["Revenue_millions"].mean(), 2)

print("Answer 3: The average revenue of movies from 2015 to 2017 in the dataset is: $",average_revenue_15to17,"million\n")


""" Question 4 """

print("Question 4: How many movies were lreleased in the year 2016?")

# count occurances of 2016 in the year column
movie_16_releases = movie_df["Year"].value_counts()[2016]

print("Answer 4:",movie_16_releases,"movies were released in 2016.\n")


""" Quesiton 5 """

print("Question 5: How many movies were directed by Christopher Nolan?")

chris_nolan_movies_no = movie_df["Director"].value_counts()["Christopher Nolan"]

print("Answer 5: Christopher Nolan directed",chris_nolan_movies_no,"movies.\n")


""" Question 6 """

print("Question 6: How many movies in the dataset have a rating of at least 8.0?")

# extract movies rated 8.0 or higher
top_rated_df = movie_df[movie_df["Rating"] >= 8.0]
# count the number of occurances
rated_8_up = top_rated_df["Rating"].count()

print("Answer 6:",rated_8_up,"movies in the dataset have a rating of at least 8.0.\n")


""" Question 7 """

print("Question 7: What is the median rating of movies directed by Christopher Nolan?")

# extract movies directed by christopher nolan
chris_nolan_movies_df = movie_df[movie_df["Director"] == "Christopher Nolan"]
# obtain the median of ratings
chris_nolan_med_rating = chris_nolan_movies_df["Rating"].median()

print("Answer 7: The median rating of the movies directed by Christopher Nolan is",chris_nolan_med_rating,".\n")


""" Question 8 """

print("Question 8: What is the year with the highest average rating?")

# group movies by year
movie_year_df = movie_df.groupby("Year")
# get the average ratings of each year group
ratings_years = movie_year_df["Rating"].mean()
# get the id (year) of the highest average rated movies
highest_rated_year = ratings_years.idxmax()

print("Answer 8: The year with the highest average rating is:",highest_rated_year,".\n")


""" Question 9 """

print("Question 9: What is the percentage increase in number of movies made between 2006 and 2016?")

# get the number of movies in 2006 and 2016
no_movies_06 = movie_df["Year"].value_counts()[2006]
no_movies_16 = movie_df["Year"].value_counts()[2016]
# calculate the percentage increase
percentage_increase_06to16 = ((no_movies_16 - no_movies_06)/(no_movies_06))*100

if percentage_increase_06to16 >= 0:
   
    print("Answer 9: The number of movies made increased by",percentage_increase_06to16,"% from 2006 to 2016.\n")
else:
    print("Answer 9: The number of movies made decreased by",percentage_increase_06to16,"% from 2006 to 2016.\n")


""" Question 10 """

print("Question 10: What is the most common actor in all the movies?")

# clear contents of the actors file before writing new data
open("actors.txt", "w").close()
# append each cell of the actors column to a text file
for i in range(movie_df["Actors"].count()):

    with open("actors.txt", "a") as actors:
        actors.write(movie_df["Actors"].loc[movie_df.index[i]])
        actors.write(", ")

# read text file back as a df, now each name is in its own cell
actors_df = pd.read_csv("actors.txt", sep=",", encoding="latin-1", header=None).transpose()

# determine the mode, and then extract that as a string
actors_mode = actors_df.mode()
most_common_actor = str(actors_mode[0].values[0])

print("Answer 10: The most common actor in all the movies is",most_common_actor,".\n")


""" Question 11 """

print("Question 11: How many unique genres are there in the dataset?")

# clear contents of the genres file before writing new data
open("Genres.txt", "w").close()
# append each cell of the genres column to a text file
for i in range(movie_df["Genre"].count()):

    with open("Genres.txt", "a") as genres:
        genres.write(movie_df["Genre"].loc[movie_df.index[i]])
        if i < (movie_df["Genre"].count()-1):
            genres.write(",")

# read text file back as a df, now each name is in its own cell
genres_df = pd.read_csv("Genres.txt", sep=",", encoding="latin-1", header=None).transpose()
# add column name
genres_df.columns =["Genres"]
# determine the number of unique values
unique_genres = genres_df.Genres.unique().size

print("Answer 11: There are",unique_genres,"unique genres in the dataset.\n")


""" Question 12 """

print("Question 12: Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.\n\nAnd what advice can you give directors to produce better movies?")

movie_df2 = pd.read_csv("movie_dataset.csv")

movie_df2.drop(["Rank"], inplace=True, axis=1)

movie_df2.columns = col_names

movie_df2.dropna(inplace = True)

movie_df_profiling = movie_df2[["Year", "Runtime_minutes", "Rating", "Votes", "Revenue_millions", "Metascore"]].copy()

profile = PR(movie_df_profiling, title=("Movies Profiling Report"))

profile.to_file("Movies_profiling_report.html")

print("Report Finished\n")


print("Answer 12:\n")
      
print("1. Between 2006 and 2012 the number of movies per year did not change significantly, however, between 2013 and 2015, there was a significant increase with the number of movies more than doubling from 2015 to 2016.\n")

print("2. Regarding run time, the the average and median were within three minutes of one another with the average at 1 hour 55 minutes. There is also a weak but noticeable correlation between movie runtime and rating, This indicates there is some preference for longer movies. From a scatterplot one can see that longer movies do not obtain a much higher maximum rating, however, they have a lower chance of having a lower rating.\n")

print("3. Longer movies although having a weak correlation to revenue, have an opportunity for a higher revenue, with the highest revenue movies being over 2 hours. However, some of the longest movies have below-average revenue.\n")

print("4. On the topic of revenue, the number of movies versus revenue decreases exponentially, furthermore, the median is roughly 36.4 million below the average of 84.6 million. Therefore, the average revenue is not a good comparator of the success of a movie, as it is largely skewed by a few high-performing movies. One should rather compare the performance of one's movie with the median for a more accurate comparison.\n")

print("5. Regarding the rating and metascore, it is apparent that the average rating is roughly 8.5 % higher than the average Metascore. It is possible that the individuals' ratings used to calculate the Metascore are more critical than the ones used to determine the rating. However, both the average and mean are closely related being within 1% of one another. It is not provided where the rating came from, however, due to the number of votes it is assumed that the rating is akin to a general audience score. This then shows that on average critics tend to score films lower than general audiences. The rating and Metascore are, however, closely correlated therefore the audiences and critics are aligned regarding how good movies are, and the general audiences just rate higher across the board.\n\n")

print("Regarding advice to directors, audiences enjoy longer movies, and with the price of going to the movies this makes sense, people want to feel they got value for their money. However, be careful to not make a movie long for the sake of length, as a long movie that is not engaging becomes a waste of time and will not play well with audiences. Also, don't get too discouraged by the reviews of critics, they tend to be somewhat over critical, also consider what the audience thinks, look at what they say, and heed their suggestions, it is after all them who pay for the movie, and they usually don't have as much of an agenda as critics.\n")


""" Question 13 """

print("This is the link to my github repository for the project:\nhttps://github.com/Joshua010403/CSS_Project_Option_1_Joshua_van_Zyl/tree/main")

