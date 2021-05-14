
# Python program to read
# json file
  
  
import urllib.request, json 
from pandas import DataFrame
import time

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=puskesmas+in+padang&key=AIzaSyCDF7PX7qn9Xd6YAcJ6KNpwxfUS7yM9pow"

with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())

npt = data["next_page_token"]
# print(npt)


time.sleep(2)

url2 = "https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={}&key=AIzaSyCDF7PX7qn9Xd6YAcJ6KNpwxfUS7yM9pow".format(npt)

with urllib.request.urlopen(url2) as jsonfile2:
    data2 = json.loads(jsonfile2.read().decode())

# print(data2)

npt2 = data2["next_page_token"]


time.sleep(2)


url3 = "https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={}&key=AIzaSyCDF7PX7qn9Xd6YAcJ6KNpwxfUS7yM9pow".format(npt2)

with urllib.request.urlopen(url3) as jsonfile3:
    data3 = json.loads(jsonfile3.read().decode())


# # print data
  
# # # Opening JSON file
# f = open('icecreamtest.json',)
  
# # returns JSON object as 
# # a dictionary
# data = json.load(f)

  
mainlist = []

# Iterating through the json
# list

for i in data['results']:
    try:
        photoreference = i["photos"][0]["photo_reference"]
    except:
        photoreference = "NULL"
        print("Photo from item number {} is unavailable from page set 1".format(i))


    smalllist = [i["name"],i["geometry"]["location"]["lat"],i["geometry"]["location"]["lng"],i["rating"],i["formatted_address"],photoreference]
    mainlist.append(smalllist)

for i in data2['results']:
    try:
        photoreference = i["photos"][0]["photo_reference"]
    except:
        photoreference = "NULL"
        print("Photo from item number {} is unavailable from page set 2".format(i))

    smalllist = [i["name"],i["geometry"]["location"]["lat"],i["geometry"]["location"]["lng"],i["rating"],i["formatted_address"],photoreference]
    mainlist.append(smalllist)

for i in data3['results']:
    try:
        photoreference = i["photos"][0]["photo_reference"]
    except:
        photoreference = "NULL"
        print("Photo from item number {} is unavailable from page set 3".format(i))

    smalllist = [i["name"],i["geometry"]["location"]["lat"],i["geometry"]["location"]["lng"],i["rating"],i["formatted_address"],photoreference]
    mainlist.append(smalllist)
  
# Closing file
# f.close()

df = DataFrame (mainlist,columns=['Name','Latitude','Longitude','rating','address','photoreference'])
print (df)

df.to_csv('puskesmas.csv')
df.to_json('puskesmas.json')