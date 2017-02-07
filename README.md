# boardgames
Board Game Recommender, and successor to BGG

## P1 FIX NOW
- [ ] bgg scrape doesn't have 'statistics' tag, which is vital
- [ ] server has some error:
    events.js:161    throw er; // Unhandled 'error' event

## MVP MVP
- [ ] site name
- [ ] grab domain, set up hosting
- [ ] learn seo, pump out articles
- [ ] scrape up to 1000 games
- [ ] set up app to take a query that is a game name, and return the data for it
- [ ] landing page, with query input
- [ ] game entry page; create and add into routes

## MVP
- [ ] JS vs db for data storage
- [ ] mailchimp
- [ ] user accounts
- [ ] users can rate games
- [ ] figure out some tracking software / site to replace this

## FEATURES TO COME
* game entry pages
  - better UI than bgg
	- link to forum for that game
* collect emails
* articles network
* user profile pages
	- collection
	- ratings
	- later on: what games they "learned more" about
* forums
* deals
* send mail to users to notify them of deals, games they might like (based on their collection and liked games), articles, events, local game stores
* video presence -- game reviews, game playthroughs, dethrone Tabletop; events coverage
	- videos need to be short; explain the overview, key mechanics, turn walkthrough, high LEVEL
	- clips of game in action, people having fun, interesting nuances
* marketplace
* kickstarter/designers hub
* subscriptions to game news, forum posts, game families
* authorities you can follow, what they are playing / posting about
* raffles/contests


## DOCUMENTS

### Articles for seo
- dominion strategy principles
- one night ultimate werewolf strategy
- personal top games lists
- gen-con roundup
- 2017 games to be excited for
- 2016 spiel de jahre recap
- captain sonar primer + rules addition
- tips for good first time captain sonar

### Recommender
- input a game you like
- algo levels:
	- LEVEL 1: rating, publisher, game type, # people, game length
	- LEVEL 2: what others who liked this own, what others who liked this also liked
	- LEVEL 3: reddit WSIG posts, users rating the link itself
- tinder/pandora/spotify-radio style swiping mechanism, shows soft landing page with: picture(s), rating, awards, price, "learn more" button, amazon affiliate link button (on picture)
	- basically enough information to get people to learn more
	- search criteria for why this game is similar to the entered one

### Other data needed
- game entry
  * picture
  * amazon affiliate link

### User profile
- name
- email
- display name
- geographic location
- collections

## REFERENCES
http://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file
https://pythonadventures.wordpress.com/2014/12/29/xml-to-dict-xml-to-json/
https://github.com/ThaWeatherman/scrapers/blob/master/boardgamegeek/get_game_info.py


## COMPETITORS
Use https://www.similarweb.com/ to test their numbers.
http://www.boardgamesfor.me/
https://boardgamegeek.com/wiki/page/Game_Recommendation_Algorithm
https://www.reddit.com/r/boardgames/comments/29wdng/announcing_the_new_board_game_recommendation_bot/
https://boardgamemenu.com/
http://stechschulte.net/2015/02/01/board-game-recommendations.html
http://meta.boardgames.stackexchange.com/questions/238/why-should-i-use-this-instead-of-boardgamegeek-whats-the-elevator-pitch

## BGG
https://www.boardgamegeek.com/xmlapi
https://www.boardgamegeek.com/thread/99401/boardgamegeek-xml-api
https://boardgamegeek.com/wiki/page/Data_Mining
https://boardgamegeek.com/wiki/page/game_entry#
