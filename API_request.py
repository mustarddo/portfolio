#-----------------------------------------------
# API requesting from JSON to CSV
# Part 1
# with Star wars API from https://swapi.dev
# Task :
# 1. Extract name, height, mass, gender, hometown of characters
# 2. Export as table in CSV

# Import library
from requests import get
from time import sleep
import pandas as pd
import matplotlib.axes as mpl


# 1) Extract name height mass gender homeworld as csv
## 1. Declare variables
url = "https://swapi.dev/api/people/"
homeurl = "https://swapi.dev/api/planets/"
starwars = []
name = []
height = []
mass = []
gender = []
home = []

# 2. API requesting 
for i in range(5):
  index = i + 1 
  web = f"{url}{index}"
  resp = get(web).json()
  name.append(resp['name'])
  height.append(int(resp['height']))
  mass.append(int(resp['mass']))
  if resp['gender'] == 'n/a':
    gender.append('uncalified')
  else: gender.append(resp['gender'])
  homeweb = f"{homeurl}{index}"
  resphw = get(homeweb).json()
  home.append(resphw['name'])
print("Starwars ready to go!!")

# 3. Store variable in DataFrame
data = {'name':name,
        'height':height ,
        'mass':mass,
        'gender':gender,
        'home':home}
starwars_df = pd.DataFrame(data)

# 4. Extract as CSV - WRITE
starwars_df.to_csv('starwars.csv')

# 5. some plotting
starwars = starwars_df.sort_values('height', ascending = False)\
    .plot(x = 'name', y = 'height', kind = 'bar', color = '#EDB120', title = 'Star wars Height Ranking')



#--------------------------------------------------------------
# Part 2
# API requesting from JSON to CSV
# with FFXIV API from https://xivapi.com
# Task :
# Extract town from FFXIV
# Clean data
# Export as table in CSV file


# 1) Find public API and extract as CSV
## Final Fantasy XIV Town list as csv

#2 API Requesting
url = "https://xivapi.com/town/"
townlist = []
for i in range (12):
  index = i + 1
  web = f"{url}{index}"
  response = get(web).json()
  if response != None:
    print(response['Name'])
  townlist.append(response['Name'])
  sleep(1)

#4 Clean and Store in DataFrame
townlist = list(filter(None, townlist))
print(townlist)
townlist_df = pd.DataFrame(townlist, columns = ['town'])
townlist_df

#5 Save as CSV
townlist_df.to_csv('ffxivtown.csv')

#--------------------------------------------------------------
