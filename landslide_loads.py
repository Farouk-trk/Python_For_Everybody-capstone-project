import json #parsing json files
import sqlite3
import urllib.request, urllib.parse, urllib.parse
import ssl
import re

conn =sqlite3.connect('landslide-data.sqlite')
cur=conn.cursor()

#create cats table to store cats data retrieved from the cats.json file in the domestic_cats database

cur.execute('''
CREATE TABLE IF NOT EXISTS Events (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT UNIQUE,
    "source" TEXT,
    "description" TEXT,
    "country" TEXT,
    "category" TEXT,
    "event_trigger" TEXT,
    "size" TEXT,
    "year" INTEGER,
    "fatality" INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
); ''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="https://data.nasa.gov/resource/dd9e-wu2v.json" #Socrata Open Data API at this URL

try:
    document=urllib.request.urlopen(url,None,30,context=ctx) #get request via Socrata Open Data API 
    text=document.read().decode() #read and decode json file
    if document.getcode() != 200 :
        print("Error code=",document.getcode(), url)
        quit()
except Exception as e:
    print("Unable to retrieve or parse page",url)
    print("Error",e)
    quit()

js=json.loads(text) #parse the JSON string
compteur=0
for event in js: #retrieve each event and insert it's data in events table
    try:
        title= event["event_title"]
        source= event["source_name"]
        description= event["event_description"]
        country= event["country_name"]
        category= event["landslide_category"]
        trigger= event["landslide_trigger"]
        size= event["landslide_size"]
        year= re.findall('([0-9]+)-',event["event_date"])[0]
        fatality= event["fatality_count"]
        compteur=compteur+1
        print(title,source,description,country,category,trigger,size,year,fatality)
        print('\n\n',compteur,'Landslide events')
    except Exception as e:
        print("missing information in",title,"Landslide.Error ",e)
        continue
    cur.execute('''
    INSERT OR IGNORE INTO Events (title, source, description, country, category, event_trigger, size, year, fatality)
    VALUES (?,?,?,?,?,?,?,?,?) ''',(title,source,description,country,category,trigger,size,year,fatality))

conn.commit()
conn.close()