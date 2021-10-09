import requests
import urllib.parse
import hashlib

from datetime import datetime
from tabulate import tabulate


#link to marvel api
marvel_api = "http://gateway.marvel.com/v1/public/characters?"

#input your marvel keys.
print("welcome to the marvel api! This script is writen by Jarne Hoefkens Student at Thomas More Geel")
public_key = input("\nEnter your marvel public key:")
Private_key = input("Enther your marvel private key:")
#timestamp is required for the marvel API otherwise you got a invalid error.
timestamp = "1"
#Hasing is required for the marvel API otherwise you got a invalid error.
before_hash = timestamp + Private_key + public_key
Hash = hashlib.md5(before_hash.encode())
#test for show the keys.
#print(public_key, Private_key)

#Print Welcome user. and quit or search function.
print("\nWelcome to my marvel api script. Let's search!")
while True:
    answ = input("\nIf you want to close this script type quit, if you want to search for a marvel comics character type search: ")
    if answ == "quit" or answ == "Quit":
        print("script wel be closed, goodbye!")
        break
        #input name for character seach.
    if answ =="search" or answ == "Search" or answ == "SEARCH":
        name = input("Marvel Character to seach for: ")
        #seach for url.
        url = marvel_api + urllib.parse.urlencode({"name": name, "ts":timestamp, "apikey":public_key, "hash":Hash.hexdigest()})
        #test for the url in json format.
        #print(url)

        #request function from json.
        data = requests.get(url).json()
        status_code = data["code"]

        #if search is succesfull (status code = 200) print name, modified, description and where it in appears.
        if status_code == 200:
            #tabulate works with tables.
            print(tabulate({"Name": [name], "Modified":[data["data"]["results"][0]["modified"]]}, headers="keys"))
            print("\n")
            print(" --- More information about " + name + " ---")
            print(str(data["data"]["results"][0]["description"]))
            print("\n")
            print(name + " Appears in the comics listed below:")
            #shows in which comics the character appears.
            for each in data["data"]["results"][0]["comics"]["items"]:
                print((each["name"]))
            print("\nStories where " + name + " in appears:")
            #shows in which stories the character appears.   
            for each in data["data"]["results"][0]["stories"]["items"]:
                print(each["name"]) 
                
        #if search is empty, ... give error.        
        elif status_code == 409:
            print("there is something wrong!")
        
    

    
                
            
        
                
    

       
