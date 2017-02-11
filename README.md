# boardgames
Board Game Recommender, and successor to BGG

## P1 FIX NOW
- [X] bgg scrape doesn't have 'statistics' tag, which is vital
- [ ] server has some error: `events.js:161    throw er; // Unhandled 'error' event`
- [ ] learn how to website architecture / infrastructure
- [ ] how to get blog into site; research other niche sites; medium embed (can't), others? jekyll?
- [ ] simplify data format

## MVP MVP MVP
- [X] site name -> **bigboardofgames.com**
- [ ] set up hosting -- digitalocean credits, calvin aws?
- [ ] learn seo, pump out articles
- [ ] scrape up to 1000 games

### MVP MVP
- [ ] set up app to take a query that is a game name, and return the data for it
- [ ] landing page, with query input
- [ ] game entry page; create and add into routes
- [ ] google analytics

## MVP
- [ ] JS vs db for data storage
- [ ] calvin wants AWS
- [ ] webpack
- [ ] mailchimp
- [ ] user accounts
- [ ] users can rate games
- [ ] figure out some tracking software / site to replace this

## FEATURES TO COME
* game entry pages
* collect emails
* articles network
* user profile pages
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
* invest in own lab to fund designers, spur innovation in the field

## DOCUMENTS

### Articles
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

### Website names
    themeta.games 12, boardgamer.space 2, metagames.io 30, metagame.io 30 metagame.space 2 metagame.world 2 boardgame.zone 3 metagaming.org 8 gamersend boardgames.tips 20 boardgames.guide 20 win condition themetagame metagame metagames gamerspace roll play victory point board game meta, gamemeter gamemeter analysis paralysis gamemaster(s) endgame gamespace gamr meeple.me game point action point sandbox ludology ludogames ludologists game mechanics dudes on a map kingmaker board game magnate board game Legacy overpowered games volksgame gamersgame

    take two board game jargons and put them together like hipster style (tasty n sons, pig and pestle, board & game)

    winning criterion: get a .com, which requires us to think bigger

### Game Entry
facebook style picture masthead, useful attributes and statistics in good UI, then user reviews a la yelp, amazon, rottentomatoes, metacritic, etc
- link to forums for those games, useful forum links (bgg, reddit), rules additions / clarifications
- other blogs pay us to link to their articles
- how to play / review videos
- user pictures
- amazon affiliate link

### Articles UI
- mtg/wizards
- medium

### User profile
- name
- email
- display name
- geographic location
- collections
- ratings
- what games they "learned more" about
- what games they click the amazon affiliate link for / ended up buying (added to collection)
- their plays
- **their comments / ratings => these will be used for other users, when they see this user's reviews/ratings, they can see what kind of player this user is, what games they own / play most often, what category is their strongest, etc**

## TODO // TOREAD
https://affiliate-program.amazon.com/
https://moz.com/beginners-guide-to-seo/how-search-engines-operate
https://www.reddit.com/r/boardgames/comments/5ppzlu/i_am_kelly_north_adams_a_female_board_game/
https://www.reddit.com/r/IAmA/comments/5st45a/iama_29yearold_married_guy_who_quit_his_job_to/
https://www.reddit.com/r/boardgames/comments/5pzb3b/my_pirate_game_tortuga_1667_raised_125k_in_its/
http://www.namemesh.com/domain-name-search/meta%20gaming?show=1
https://www.smashingmagazine.com/2009/05/the-effective-strategy-for-choosing-right-domain-names/



## REFERENCES
http://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file
https://pythonadventures.wordpress.com/2014/12/29/xml-to-dict-xml-to-json/
https://github.com/ThaWeatherman/scrapers/blob/master/boardgamegeek/get_game_info.py
http://blog.joanboixados.com/building-a-boilerplate-for-a-koa-redux-react-application-including-webpack-mocha-and-sass/
http://www.industrydive.com/news/post/how-to-make-html-email-buttons-that-rock/#outlook


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
https://www.reddit.com/r/boardgames/comments/2no1ko/i_dont_get_boardgamegeekcom/
https://www.reddit.com/r/boardgames/comments/1tht4h/my_personal_guide_to_boardgamegeek_how_i_make_the/
