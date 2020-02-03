
import numpy as np
import pandas as pd
import re

# Importing the initial dataframe
df = pd.read_csv("input/tmdb_5000_movies.csv")

# Selection of the variables of interest.
# Column "title" is preferred over "original_title" for an easier search.

df2 = df[["title", "genres", "overview", "release_date", "vote_average"]]

# Removal of rows with NaN values.

df3 = df2.dropna()

# Arrangement of the "genres" column using eval().

string_to_dict = lambda x: [e["name"] for e in eval(x)]
df2["genres"] = df2["genres"].apply(string_to_dict)

# Arrangement of the "release_date" column just to receive the Year.

date = [re.findall("[0-9]{4}", str(e)) for e in df3['release_date']]
date2 = [i for e in date for i in e] #flattened
df3["Year"] = date2
df4 = df3.drop(labels = "release_date", axis = 1)

# Renaming of the columns for a better interpretation.

columns = {"original_title": "Title", "genres": "Genre", "overview": "Overview", "vote_average": "Rating"}
df4 = df4.rename(columns = columns)

# Applying API and scraping functions to enrich our dataframe.
# I am dividing the dataframe into pieces due to computing performance.

df1 = dataf.iloc[:100].copy()
for name, func in newColumns.items():
    df1[name] =  df1.apply(lambda x: newSeries(x,func), axis=1)

df2 = dataf.iloc[100:300].copy()
for name, func in newColumns.items():
    df2[name] =  df2.apply(lambda x: newSeries(x,func), axis=1)

df3 = dataf.iloc[300:500].copy()
for name, func in newColumns.items():
    df3[name] =  df3.apply(lambda x: newSeries(x,func), axis=1)

df4 = dataf.iloc[500:800].copy()
for name, func in newColumns.items():
    df4[name] =  df4.apply(lambda x: newSeries(x,func), axis=1)

df5 = dataf.iloc[800:1001].copy()
for name, func in newColumns.items():
    df5[name] =  df5.apply(lambda x: newSeries(x,func), axis=1)

# Merging all those dataframes to create a 1000 records dataframe.

manyDfs = [df1, df2, df3, df4, df5]
thousandRecords = pd.concat(manyDfs) 
thousandRecords = thousandRecords.drop(labels = "Unnamed: 0", axis = 1)

# Dataframe export in .csv format

thousandRecords.to_csv('output/thousandRecords.csv', index=False)


