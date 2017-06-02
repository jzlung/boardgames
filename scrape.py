import requests
import xmltodict
import json
import time
import collections
import shutil
import re

### Given a list of gameIds, which is BGG's only way to access the full stats
### of a game in its API, sc. Run via:
### python3 scrape.py

API_URL = "https://boardgamegeek.com/xmlapi/boardgame/"

gameIds = [
    161936, # Pandemic Legacy
    120677, # Terra Mystica
    173346, # 7 Wonders Duel
    84876, # The Castles of Burgundy
    2651, # Power Grid
]

DIR_IMAGES = "images/"
DIR_THUMBS = DIR_IMAGES + "thumbnails/"

# Assumes array of objects with a #text field that we want
def map_deconstruct(arr_of_objects):
    res = []
    for obj in arr_of_objects:
        res.append(obj['#text'])
    return res

def extract_replace(orig_name, new_name):
    if orig_name in pee:
        temp = pee.pop(orig_name)
        if not isinstance(temp, list):
            temp = [ temp ]
        pee[new_name] = map_deconstruct(temp)

file = open("full_out.json", "w")
objectToJson = {}
objectToJson["gameList"] = []
# Modify this limit to your liking
limit = 200
count = 0

gameList = open("items.csv")
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
    name = pee['name']
    name_sanitized = re.sub(r'[:!?,`"\'&/ ]', '', name)

    # boardgamecategory is actually themes, which is not useful imho; use subdomain instead
    if 'boardgamecategory' in pee:
        pee.pop('boardgamecategory')
    extract_replace('boardgamesubdomain', 'categories')
    extract_replace('boardgamefamily', 'families')
    if 'families' in pee:
        families = pee.pop('families')
        pee['categories'].extend(families)
    sanitized_categories = []
    if 'Pandemic' in name:
        pee['categories'].append('Cooperative')
    for category in pee['categories']:
        if 'Thematic' in category:
            continue
        # TODO: maybe have to extend this to " Game", " games", etc
        if category.lower().endswith(' games'):
            category = category[:-len(' games')]
        sanitized_categories.append(category)
    pee['categories'] = sanitized_categories

    # designers
    extract_replace('boardgamedesigner', 'designers')

    # artists
    extract_replace('boardgameartist', 'artists')

    # boardgamemechanic
    extract_replace('boardgamemechanic', 'mechanics')

    # boardgamemechanic
    extract_replace('boardgamepublisher', 'publishers')

    extract_replace('boardgamehonor', 'awards')

    extract_replace('boardgameimplementation', 'derived_from')

    extract_replace('videogamebg', 'videogamebg')

    # Expansions link to other games; useful to have the IDs
    # extract_replace('boardgameexpansion', 'expansions')

    extract_replace('boardgameaccessory', 'accessories')

    extract_replace('boardgamecompilation', 'compilations')


    # # TODO: hack
    # if pee['name'] == "Pandemic Legacy: Season 1":
    #     cooperative = {};
    #     cooperative["@objectid"] = "999992";
    #     cooperative["#text"] = "Cooperative"
    #     legacy = {};
    #     legacy["@objectid"] = "999991";
    #     legacy["#text"] = "Legacy";
    #     pee['categories'].append(cooperative);
    #     pee['categories'].append(legacy);

    # Download the images to file
    image_url = pee['image']
    file_ext = image_url.split('.')[-1]
    image_filename = name_sanitized + '.' + file_ext
    image_response = requests.get(image_url, stream=True)
    with open(DIR_IMAGES + image_filename, 'wb') as out_file:
        shutil.copyfileobj(image_response.raw, out_file)
    del image_response
    pee['image'] = image_filename

    # Thumbnails; do the same as images
    thumb_url = pee['thumbnail']
    file_ext = thumb_url.split('.')[-1]
    thumb_filename = name_sanitized + '-thumbnail.' + file_ext
    thumb_response = requests.get(thumb_url, stream=True)
    with open(DIR_THUMBS + thumb_filename, 'wb') as out_file:
        shutil.copyfileobj(thumb_response.raw, out_file)
    del thumb_response
    pee['thumbnail'] = thumb_filename

    # The following methods move the fields around so the JSON is better readable;
    pee.move_to_end('name',last=False)
    if 'boardgamehonor' in pee:
        pee.move_to_end('boardgamehonor')
    # Description is pretty important but moving to end is a good way to delineate one entry from another
    pee.move_to_end('description')
    pee.move_to_end('@objectid', last=False)

    objectToJson["gameList"].append(pee)
    # BGG API will reject if you make too any requests too quickly
    time.sleep(2)

poop = json.dumps(objectToJson, indent=2, separators=(',', ': '))
print("Writing to file...")
file.write(poop + '\n')

file.close();



'''
      const pandemicLegacy = {
        // @objectid -> id
        "@objectid": "161936",
        "name": "Pandemic Legacy: Season 1",
        // yearpublished -> year
        "yearpublished": "2015",
        "minplayers": "2",
        "maxplayers": "4",
        "playingtime": "60",
        "minplaytime": "60",
        "maxplaytime": "60",
        "age": "13",
        // TODO: download
        "thumbnail": "//cf.geekdo-images.com/images/pic2452831_t.png",
        // TODO: download
        "image": "pandemiclegacy.png",
        // boardgamefamily -> family
        "boardgamefamily": [
          {
            "@objectid": "24281",
            // #text -> text
            "#text": "Campaign Games"
          },
          {
            "@objectid": "25404",
            "#text": "Legacy"
          },
          {
            "@objectid": "3430",
            "#text": "Pandemic"
          }
        ],
        // boardgamedesigner -> designer
        "boardgamedesigner": [
          {
            "@objectid": "442",
            "#text": "Rob Daviau"
          },
          {
            "@objectid": "378",
            "#text": "Matt Leacock"
          }
        ],
        // delete boardgamecategory
        "boardgamecategory": [
          {
            "@objectid": "1084",
            "#text": "Environmental"
          },
          {
            "@objectid": "2145",
            "#text": "Medical"
          }
        ],
        // boardgameartist -> artist
        "boardgameartist": {
          "@objectid": "14057",
          "#text": "Chris Quilliams"
        },
        "categories": [
          {
            "@objectid": "5497",
            "#text": "Strategy"
          },
          // TODO: I added these manually
          {
            "@objectid": "999992",
            "#text": "Cooperative"
          },
          {
            "@objectid": "999991",
            "#text": "Legacy"
          }
        ],
        // boardgameimplementation -> implementation
        "boardgameimplementation": {
          "@objectid": "30549",
          "@inbound": "true",
          "#text": "Pandemic"
        },
        "statistics": {
          "@page": "1",
          "ratings": {
            "usersrated": "15037",
            "average": "8.65931",
            "bayesaverage": "8.46644",
            "ranks": {
              "rank": [
                {
                  "@type": "subtype",
                  "@id": "1",
                  "@name": "boardgame",
                  "@friendlyname": "Board Game Rank",
                  "@value": "1",
                  "@bayesaverage": "8.46644"
                },
                {
                  "@type": "family",
                  "@id": "5496",
                  "@name": "thematic",
                  "@friendlyname": "Thematic Rank",
                  "@value": "1",
                  "@bayesaverage": "8.48497"
                },
                {
                  "@type": "family",
                  "@id": "5497",
                  "@name": "strategygames",
                  "@friendlyname": "Strategy Game Rank",
                  "@value": "1",
                  "@bayesaverage": "8.46704"
                }
              ]
            },
            "stddev": "1.77846",
            "median": "0",
            "owned": "24966",
            "trading": "91",
            "wanting": "610",
            "wishing": "5513",
            "numcomments": "2645",
            "numweights": "573",
            "averageweight": "2.808"
          }
        },
        // boardgamemechanic -> mechanics
        "boardgamemechanic": [
          {
            "@objectid": "2001",
            "#text": "Action Point Allowance System"
          },
          {
            "@objectid": "2023",
            "#text": "Co-operative Play"
          },
          {
            "@objectid": "2040",
            "#text": "Hand Management"
          },
          {
            "@objectid": "2078",
            "#text": "Point to Point Movement"
          },
          {
            "@objectid": "2004",
            "#text": "Set Collection"
          },
          {
            "@objectid": "2008",
            "#text": "Trading"
          },
          {
            "@objectid": "2015",
            "#text": "Variable Player Powers"
          }
        ],
        // boardgamepublisher -> publisher
        "boardgamepublisher": [
          {
            "@objectid": "538",
            "#text": "Z-Man Games"
          },
          {
            "@objectid": "15889",
            "#text": "Asterion Press"
          },
          {
            "@objectid": "2366",
            "#text": "Devir"
          },
          {
            "@objectid": "5657",
            "#text": "Filosofia \u00c9ditions"
          },
          {
            "@objectid": "8820",
            "#text": "G\u00e9m Klub Kft."
          },
          {
            "@objectid": "1391",
            "#text": "Hobby Japan"
          },
          {
            "@objectid": "15983",
            "#text": "Jolly Thinkers"
          },
          {
            "@objectid": "5812",
            "#text": "Lacerta"
          },
          {
            "@objectid": "9325",
            "#text": "Lifestyle Boardgames Ltd"
          },
          {
            "@objectid": "7992",
            "#text": "MINDOK"
          }
        ],
        "boardgamehonor": [
          {
            "@objectid": "34506",
            "#text": "2015 Golden Geek Best Innovative Board Game Nominee"
          },
          {
            "@objectid": "34781",
            "#text": "2015 Golden Geek Best Innovative Board Game Winner"
          },
          {
            "@objectid": "34510",
            "#text": "2015 Golden Geek Best Strategy Board Game Nominee"
          },
          {
            "@objectid": "34785",
            "#text": "2015 Golden Geek Best Strategy Board Game Winner"
          },
          {
            "@objectid": "34511",
            "#text": "2015 Golden Geek Best Thematic Board Game Nominee"
          },
          {
            "@objectid": "34786",
            "#text": "2015 Golden Geek Best Thematic Board Game Winner"
          },
          {
            "@objectid": "34500",
            "#text": "2015 Golden Geek Board Game of the Year Nominee"
          },
          {
            "@objectid": "34775",
            "#text": "2015 Golden Geek Board Game of the Year Winner"
          },
          {
            "@objectid": "37315",
            "#text": "2015 Meeples' Choice Nominee"
          },
          {
            "@objectid": "35436",
            "#text": "2016 As d'Or - Jeu de l'Ann\u00e9e Expert Nominee"
          },
          {
            "@objectid": "35437",
            "#text": "2016 As d'Or - Jeu de l'Ann\u00e9e Expert Winner"
          },
          {
            "@objectid": "36910",
            "#text": "2016 Diana Jones Award for Excellence in Gaming Nominee"
          },
          {
            "@objectid": "34820",
            "#text": "2016 Goblin Magnifico Nominee"
          },
          {
            "@objectid": "37769",
            "#text": "2016 International Gamers Award - General Strategy: Multi-player Nominee"
          },
          {
            "@objectid": "35994",
            "#text": "2016 Kennerspiel des Jahres Nominee"
          },
          {
            "@objectid": "36040",
            "#text": "2016 SXSW Tabletop Game of the Year Winner"
          }
        ],
        "description": "Pandemic Legacy is a co-operative campaign game, with an overarching story-arc played through 12-24 sessions, depending on how well your group does at the game. At the beginning, the game starts very similar to basic Pandemic, in which your team of disease-fighting specialists races against the clock to travel around the world, treating disease hotspots while researching cures for each of four plagues before they get out of hand.<br/><br/>During a player's turn, they have four actions available, with which they may travel around in the world in various ways (sometimes needing to discard a card), build structures like research stations, treat diseases (removing one cube from the board; if all cubes of a color have been removed, the disease has been eradicated), trade cards with other players, or find a cure for a disease (requiring five cards of the same color to be discarded while at a research station). Each player has a unique role with special abilities to help them at these actions.<br/><br/>After a player has taken their actions, they draw two cards. These cards can include epidemic cards, which will place new disease cubes on the board, and can lead to an outbreak, spreading disease cubes even further. Outbreaks additionally increase the panic level of a city, making that city more expensive to travel to.<br/><br/>Each month in the game, you have two chances to achieve that month's objectives. If you succeed, you win and immediately move on to the next month. If you fail, you have a second chance, with more funding for beneficial event cards.<br/><br/>During the campaign, new rules and components will be introduced. These will sometimes require you to permanently alter the components of the game; this includes writing on cards, ripping up cards, and placing permanent stickers on components. Your characters can gain new skills, or detrimental effects. A character can even be lost entirely, at which point it's no longer available for play.<br/><br/>"
      };
'''
