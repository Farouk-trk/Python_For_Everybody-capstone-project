import sqlite3

conn = sqlite3.connect('landslide-data.sqlite')
cur = conn.cursor()

#extract the list of countries from the database
cur.execute('SELECT country FROM Events')
countries = list()
for message_row in cur :
    if message_row[0] not in countries:
        countries.append(message_row[0])

#extract the list of years from the database
cur.execute('SELECT year FROM Events')
years = list()
for message_row in cur :
    if message_row[0] not in years:
        years.append(message_row[0])
print(sorted(years))