import pandas as pd

# question 1 - read the csv file into the variable df
df = pd.read_csv("movies_data.csv")
# show the top 5 rows
print(df.head(5))

# question 2 - add a new column called year_classify
# then create new values where if, release_year is less than 2000, then 'before 2000' or else 'From 2000'


def year_classification(classification):
    if classification < 2000:
        return 'Before 2000'
    else:
        return 'From 2000'


df["year_classify"] = df['release_year'].apply(year_classification)
print(df.head(4))

# question 3 - Save the above dataframe with the name "final_movie_data.csv" and include
# only columns 'movie_id', 'title', 'budget', 'revenue' and 'year_classify'.
# Also set index to False**.
df.to_csv("final_movie_data.csv", columns=['movie_id', 'title', 'budget', 'revenue', 'year_classify'], index=False)
