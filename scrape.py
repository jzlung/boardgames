import requests
import xmltodict
import json

### Given a list of gameIds, which is BGG's only way to access the full stats
### of a game in its API, scrapes the XML data for the game and turns it into json.
### REQUIRES PYTHON 3

API_URL = "https://boardgamegeek.com/xmlapi/boardgame/";

gameIds = [
    161936, # Pandemic Legacy
    120677, # Terra Mystica
    173346, # 7 Wonders Duel
    84876, # The Castles of Burgundy
    2651, # Power Grid
]

file = open("full_out.json", "w")
objectToJson = {};
objectToJson["gameList"] = [];

for gameId in gameIds:
    page = requests.get(API_URL + str(gameId))
    # poop = json.dumps(xmltodict.parse(page.text), indent=2, separators=(',', ': '))
    butt = xmltodict.parse(page.text)

    # preprocess
    pee = butt['boardgames']['boardgame']
    pee.pop('boardgamepodcastepisode', None)
    pee.pop('boardgameversion', None)
    pee.pop('rpgpodcastepisode', None)
    pee.pop('poll', None)
    for i in range(len(pee['name'])):
        if '@primary' in pee['name'][i]:
            pee['name'] = pee['name'][i]['#text']
            break
    ## The following methods move the fields around so the JSON is better readable;
    ## Slight error right now using python 2.7.13: AttributeError: 'OrderedDict' object has no attribute 'move_to_end'
    pee.move_to_end('name',last=False)
    pee.move_to_end('boardgamemechanic')
    pee.move_to_end('boardgamepublisher')
    pee.move_to_end('boardgamehonor')
    ## Debated right now, description is pretty important but moving to end is a good way to delineate one entry from another
    pee.move_to_end('description')
    pee.move_to_end('@objectid', last=False)
    objectToJson["gameList"].append(pee);

poop = json.dumps(objectToJson, indent=2, separators=(',', ': '))
file.write(poop + '\n')

file.close();
