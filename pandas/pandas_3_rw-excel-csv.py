import pandas as pd
# install pandas in the interpreter
# ------CSV--------
# view data and assign data to a dataframe
df = pd.read_csv("stock_data.csv")
# skip the first row which has non-meaningful data as row headers
df2 = pd.read_csv("stock_data.csv", skiprows=1)
print(df2)
# this code tells you which row to assign as the row header
df3 = pd.read_csv("stock_data.csv", header=1)

# give a custom column name
df7 = pd.read_csv("stock_data.csv", header=1, names=["stock_symbol", "eps", "revenue", "price", "people"])
print(df7)

# specify how many rows you want to read
df4 = pd.read_csv("stock_data.csv", header=1, nrows=4)
print(df4)

# convert NA values to proper NaN (= not available) values in each specified column
df5 = pd.read_csv("stock_data.csv", header=1,
                  na_values={'eps': ['not available'], 'revenue': [-1], 'people': ['not available', 'n.a.']})
print(df5)

# convert NA values to proper NaN (= not available) values in each cell that is specified
df6 = pd.read_csv("stock_data.csv", header=1,
                  na_values=['not available', -1, 'n.a.'])

# Convert 'price' and 'eps' columns to numeric types (there was an error, so I introduced these two lines of code)
df7['price'] = pd.to_numeric(df7['price'], errors='coerce')
df7['eps'] = pd.to_numeric(df7['eps'], errors='coerce')
# create a new column with a derived value
df7["pe"] = df7["price"] / df7["eps"]
print(df7)

# export the above file to a csv file
df7.to_csv("pe.csv")

# remove index column. This does not update the same file, so you may want to create a new file
df7.to_csv("pe1.csv", index=False)

# remove header row from the dataset for some analysis
# df7.to_csv("pe1.csv", index=False, header=False)

# -------EXCEL---------
# install openpyxl method in the console

# read the Excel file and open the sheet movies
df_movies = pd.read_excel("movies_db.xlsx", "movies")
print(df_movies.head(4))

# read the Excel file and open the sheet financials
df_fin = pd.read_excel("movies_db.xlsx", "financials")
print(df_fin.head(4))

# make all the currency values USD, and not other representatives
# we write a function first to convert the currency value to a standardized value


def standardize_currency(curr):
    if curr == "$$" or curr == "Dollars":
        return "USD"
    return curr


df_fin = pd.read_excel("movies_db.xlsx", "financials", converters={'currency': standardize_currency})
print(df_fin.head(4))

# merge two dataframes based on movie_id column
df_merged = pd.merge(df_movies, df_fin, on="movie_id")
print(df_merged)

# export to an Excel file
df_merged.to_excel("movies_merged.xlsx", sheet_name="merged", index=False)

# create a dataframe using a dictionary, and merge them together in two sheets in Excel.
# in the following example, two dataframes are created and merged.
df_stocks = pd.DataFrame({
    'stock_symbol': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})
print(df_stocks)

df_weather = pd.DataFrame({
    'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
    'temperature': [32, 35, 28],
    'event': ['Rain', 'Sunny', 'Snow'],
})
print(df_weather)

# use an api 'ExcelWriter' to combine or merge two above tables into separate sheets in one workbook
with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
