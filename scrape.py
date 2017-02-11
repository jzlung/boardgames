import requests
import xmltodict
import json
import time
import collections

### Given a list of gameIds, which is BGG's only way to access the full stats
### of a game in its API, scrapes the XML data for the game and turns it into json.
### REQUIRES PYTHON 3

API_URL = "https://boardgamegeek.com/xmlapi/boardgame/"

gameIds = [
    161936, # Pandemic Legacy
    120677, # Terra Mystica
    173346, # 7 Wonders Duel
    84876, # The Castles of Burgundy
    2651, # Power Grid
]

# file = open("full_out.json", "w")
file = open("test.json", "w")
objectToJson = {}
objectToJson["gameList"] = []
# Modify this limit to your liking
limit = 100
count = 0

gameList = open("games.csv")
for line in gameList:
    # First line is header, so discount it
    if count == limit + 1:
        break
    count = count + 1
    if count == 1:
        continue
    gameId = line.split(",")[-1]
    print(line.split(",")[1])
    page = requests.get(API_URL + str(gameId) + '?stats=1')
    # poop = json.dumps(xmltodict.parse(page.text), indent=2, separators=(',', ': '))
    butt = xmltodict.parse(page.text)
    pee = butt['boardgames']['boardgame']


    # preprocess: remove unneeded info
    pee.pop('boardgamepodcastepisode', None)
    pee.pop('boardgameversion', None)
    pee.pop('rpgpodcastepisode', None)
    pee.pop('poll', None)
    if type(pee['name']) is list:
        for i in range(len(pee['name'])):
            if '@primary' in pee['name'][i]:
                pee['name'] = pee['name'][i]['#text']
                break
    elif type(pee['name']) is collections.OrderedDict:
        pee['name'] = pee['name']['#text']

    # Process boardgamesubdomain into categories, and then sanitize by removing unnecessary qualifiers
    pee['categories'] = pee.pop('boardgamesubdomain')
    # boardgamecategory is actually themes, which is not useful imho
    pee.pop('boardgamecategory')
    if isinstance(pee['categories'], list):
        for category in pee['categories']:
            # TODO: maybe have to extend this to " Game", " games", etc
            if category['#text'].endswith(' Games'):
                category['#text'] = category['#text'][:-len(' Games')]
        pee['categories'][:] = [category for category in pee['categories'] if not category['#text'] == "Thematic"]
    else:
        if pee['categories']['#text'].endswith(' Games'):
            category['#text'] = category['#text'][:-len(' Games')]

    # TODO: hack
    if pee['name'] == "Pandemic Legacy: Season 1":
        cooperative = {};
        cooperative["@objectid"] = "999992";
        cooperative["#text"] = "Cooperative"
        legacy = {};
        legacy["@objectid"] = "999991";
        legacy["#text"] = "Legacy";
        pee['categories'].append(cooperative);
        pee['categories'].append(legacy);

    # TODO: download the image and change image url to new local image url
    pee['image'] = "pandemiclegacy.png"

    ## The following methods move the fields around so the JSON is better readable;
    ## Slight error right now using python 2.7.13: AttributeError: 'OrderedDict' object has no attribute 'move_to_end'
    pee.move_to_end('name',last=False)
    pee.move_to_end('boardgamemechanic')
    pee.move_to_end('boardgamepublisher')
    if 'boardgamehonor' in pee:
        pee.move_to_end('boardgamehonor')
    ## Debated right now, description is pretty important but moving to end is a good way to delineate one entry from another
    pee.move_to_end('description')
    pee.move_to_end('@objectid', last=False)
    objectToJson["gameList"].append(pee)
    time.sleep(2)

poop = json.dumps(objectToJson, indent=2, separators=(',', ': '))
print("Writing to file...")
file.write(poop + '\n')

file.close();
