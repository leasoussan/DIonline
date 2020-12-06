
import sqlite3
import requests
import json
import random 
import psycopg2
import pprint









# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(country.json())






countries_api = requests.get('https://restcountries.eu/rest/v2/all') 

countries = countries_api.json()

pprint.pprint(type(countries))


# print(country)


name = countries['name']
flag = name['flag']
subregion = name['subregion']
population = name['population']
print(name)
print(subregion)


conn = sqlite3.connect('country.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS countries")

c.execute("CREATE TABLE countries (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, flag link VarChar(200) NOT NULL, subregion VARCHAR(50) NOT NULL, population INTEGER)")

for country in countries: 
        c.execute("INSERT INTO countries (name, flag,subregion, population) VALUES ('{name}', '{flag}', '{subregion}', '{population}') ")

        conn.commit()
conn.close()        