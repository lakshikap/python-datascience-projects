import pandas as pd
# read the movies csv file and assign it to a dataframe
df = pd.read_csv("movies.csv")
# print the first 3 rows in the dataframe
print(df.head(3))
# print all the columns in the dataframe
print(df.columns)

# check how many unique values or industry types are in the industry column
print(df.industry.unique())
print(df['language'].unique())
# count the number of values in the industry column
print(df.industry.value_counts())
# count of languages in the dataset
print(df.language.value_counts())
# column filtering - create a new dataframe with a subset of columns from the df dataframe
print(df[["title", "imdb_rating", "industry"]])

# print all movies between 2000 and 2010 using AND condition
print(df[(df.release_year >= 2000) & (df.release_year <= 2010)])
# see movies only from Marvel studios
print(df[df.studio == "Marvel Studios"])

# print all the like nulls and data type in relation to the columns
print(df.info())
# print data descriptions for numerical columns like count, mean std, min, max and quartiles
print(df.describe())

# basic data analysis
# print movie with max and min imdb rating and
print(df[df.imdb_rating == df.imdb_rating.max()])
print(df[df.imdb_rating == df.imdb_rating.min()])
# another method for the same, but using OR condition
ratings = df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())]

# generate new columns with a derived value (age of a movie)
df["age"] = df['release_year'].apply(lambda x: 2024-x)
print(df.head(4))

# add a new column and calculate profit of a movie
df["profit"] = df.apply(lambda x: x['revenue'] - x['budget'], axis=1)
print(df.head(4))

# range of indexes in the dataframe
print(df.index)
# set movie title column as zero index over the row number
df.set_index("title", inplace=True)
print(df.head(3))
# benefit is when I print is, the movie titles appear when I type the next code
print(df.index)
# prints all the attributes in rows for the following movie
print(df.loc["Pather Panchali"])
# index is like a hashmap or like a dictionary

# print multiple rows using index
print(df.loc[["Pather Panchali", "Doctor Strange in the Multiverse of Madness"]])

# integer based location or index
print(df.iloc[0])
print(df.iloc[2:6])
