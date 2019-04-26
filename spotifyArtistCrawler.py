import requests
import json
import urllib.parse

# Add lineup array here ["Childish Gambino", "Ariana Grande"]
# Text is urlencoded for requests

# If an exact search for the artist name does not show, use their artistid.
# For example, Blond:ish is not searchable due to the colon. 
# Find her spotify artist page on the Spotify web app and place https://api.spotify.com/v1/artists/<ARTIST_ID> in the array.

artists = [
    "Disclosure",
    "Big Gigantic",
    "Flying Lotus",
    "Santigold",
    "Gramatik",
    "Toro Y Moi",
    "Khruangbin",
    "Lane 8",
    "DJ Koze",
    "Damian Lazarus",
    "Shiba San",
    "Bedouin",
    "G Jones",
    "The Polish Ambassador",
    "Opiuo",
    "Clozee",
    "Rising Appalachia",
    "Masego",
    "Elohim",
    "Cautious Clay",
    "Recondite",
    "Escapade",
    "Rampue",
    "Shades",
    "1788-L",
    "Desert Dwellers",
    "CharlesTheFirst",
    "Jan Blomqvist",
    "Channel Tres",
    "Frameworks",
    "https://api.spotify.com/v1/artists/7hwZLbYVax5K8GvRSmRSOF",
    "https://api.spotify.com/v1/artists/7gO5Zxv0gQXMTkus0ro8tj",
    "Mobley",
    "Slenderbodies",
    "Nico Stojan",
    "Doc Martin",
    "Luttrell",
    "Osunlade",
    "Gorje Hewek",
    "izhevski",
    "Holmar",
    "Omnom",
    "Vnssa",
    "Anton Tumas",
    "Zach Walker",
    "Duchess",
    "Dimond Saints",
    "Spectrasoul",
    "SP:MC",
    "https://api.spotify.com/v1/artists/1YLeUsNujSB7Fp1tnCWZi2",
    "Axel Thesleff",
    "Joe Kay",
    "Sasha Marie",
    "Manatee Commune",
    "Soohan",
    "Ill-esha",
    "Pigeon Hole",
    "Megan Hamilton",
    "Dorfex Bos",
    "Kll Smth",
    "Anna Morgan",
    "Mat the Alien",
    "Aabo",
    "Prsn",
    "Red Giant",
]

artistOutput = []
# Use an auth token from here: https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset=
# On the last input field "Get Token"
authToken = "BQC4OItwvbIVk4nlc1_QZCuMghrrYQaQRO9ewgeobfPe7kZqJRa6Jntkdyde78-MRYCDjQ5Wq-4eZzj7PHAxFcl-hW3RiO90dvQNlrvIwE1b5IvmA7zn6KThPm8LE18lHSyBWZc50uSnC4nlNA"
headers = {"Authorization": "Bearer " + authToken}

for artist in artists:
    if not "https://api" in artist:
        urlencodedArtist = urllib.parse.quote_plus(artist)
        req = requests.get(
            "https://api.spotify.com/v1/search?q=" + str(urlencodedArtist) + "&type=artist", headers=headers)
        if not req.ok:
            print(req)
            print("Check your auth token!")
            break;

        res = req.json()
        
        if len(res["artists"]["items"]) < 1:
            print(artist + " did not find any results!")
            continue;

        firstResult = res["artists"]["items"][0]
        res["artists"]["items"] = [firstResult]
        artistOutput.append(res)
        print(artist)
    else:
        # Search for specific artist with given artistID with URL since some artists are not detected using their full name (Ex: Blond:ish)
        req = requests.get(artist, headers=headers)
        artistsDict = {}
        artistsDict['artists'] = {'items': [req.json()]}
        artistOutput.append(artistsDict)
        print(artist)

with open('artistsOutput.json', 'w') as outputFile:
    json.dump(artistOutput, outputFile, indent=4)
