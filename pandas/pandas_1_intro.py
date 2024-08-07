# import the pandas library
import pandas as pd

# import the dataset csv file and assign it to a dataframe df
df = pd.read_csv("movies.csv")
# print the first 7 rows (from index = 0 to 6)
print(df.head(7))
# print the last three rows in the dataset
print(df.tail(3))
# print a data sample of 5 rows picked randomly
print(df.sample(5))
# print rows from 2 to 5
print(df[2:6])
# print the total number of rows and columns in the dataset
print(df.shape)

# print a column called imdb rating as an index operator
print(df["imdb_rating"])
# print a column called imdb rating as a property (class object and property)
print(df.imdb_rating)

# the column in a dataframe object is called a series, and it prints the type here
print(type(df.imdb_rating))
# the type of the dataframe
print(type(df))
# print all the properties of the dataframe or column in the dataframe
print(dir(df))

# print min, max and mean of a column in the dataframe
print(df.imdb_rating.min())
print(df.imdb_rating.max())
print(df.imdb_rating.mean())

# print only hollywood or bollywood movies from the dataframe
# use a condition to filter the dataset
# assign the separated dataset to a new dataframe
df_b = df[df.industry == "Bollywood"]
print(df_b)
df_h = df[df.industry == "Hollywood"]
print(df_h)

# print the min, max and mean of Bollywood movies' imdb rating
print(df_b.imdb_rating.min())
print(df_b.imdb_rating.max())
print(df_b.imdb_rating.mean())
# print the min, max and mean of Hollywood movies' imdb rating
print(df_h.imdb_rating.min())
print(df_h.imdb_rating.max())
print(df_h.imdb_rating.mean())

# complete code of pandas analysis
df = pd.read_csv("movies.csv")
print("All movies: Min=", df.imdb_rating.min(), "Max=", df.imdb_rating.max(), "Mean=", df.imdb_rating.mean())

df_b = df[df.industry == "Bollywood"]
df_h = df[df.industry == "Hollywood"]

print("Bollywood movies: Min=", df_b.imdb_rating.min(),
      "Max=", df_b.imdb_rating.max(), "Mean=", df_b.imdb_rating.mean())
print("Hollywood movies: Min=", df_h.imdb_rating.min(),
      "Max=", df_h.imdb_rating.max(), "Mean=", df_h.imdb_rating.mean())
