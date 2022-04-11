import sqlite3
import pandas as pd

conn = sqlite3.connect('apartments.db')
cur = conn.cursor()
query = "SELECT * FROM apartments"
df = pd.read_sql(query, conn)

df[['city', 'district']] = (df['title']
    .str.replace("śląskie,", " ")
    .str.strip()
    .str.split(pat=',', n=1, expand=True)
 )

df.drop('title', axis=1, inplace=True)

df[['rooms', 'sq_m', 'floor']] = (df['ro_sp_fl']
     .str.split('-', expand=True)
     .loc[:,[0,2,5]]
)

df.drop('ro_sp_fl', axis=1, inplace=True)

df[['price', 'rooms', 'sq_m']] = df[['price', 'rooms', 'sq_m']].astype(int)

df.info()

str = '\nRybnik, Niedobczyce '
str.replace("śląskie,", "").strip().split(", ", 1)