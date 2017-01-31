# boardgames
Board Game Recommender, and successor to BGG


bgg

1st steps
	seo
		- "games similar to..."
	scrape the fuck out of bgg
	build the bare bones app
	write articles for seo
		- dominion strategy principles
		- one night ultimate werewolf strategy
		- personal top games lists
		- gen-con roundup
		- 2017 games to be excited for
		- 2016 spiel de jahre recap
		- captain sonar rules addition
		- tips for good first time captain sonar

recommender
	- input a game you like
	- algo:
		- LEVEL 1: rating, publisher, game type, # people, game length
		- LEVEL 2: what others who liked this own, what others who liked this also liked
		- LEVEL 3: reddit WSIG posts, users rating the link itself
	- tinder/pandora/spotify-radio style swiping mechanism, shows soft landing page with: picture(s), rating, awards, price, "learn more" button, amazon affiliate link button (on picture)
		- basically enough information to get people to learn more
		- search criteria for why this game is similar to the entered one



DATA NEED TO SCRAPE
	game entry
		picture
		name
		rating
		game type / categories
		game length
		# players
		awards won
		amazon affiliate link


	user collections




OTHER FEATURES TO COME

	game entry pages
		- better UI than bgg
		- link to forum for that game

	user profile pages
		- collection
		- ratings
		- later on: what games they "learned more" about

	subscriptions to game news, forum posts, game families

	raffles/contests

	deals

	forums

	marketplace

	kickstarter/designers hub

	articles network

	authorities you can follow, what they are playing / posting about

  send mail to users to notify them of deals, games they might like (based on their collection and liked games), articles, events, local game stores

	video presence -- game reviews, game playthroughs, dethrone Tabletop; events coverage



REFERENCES
http://stackoverflow.com/questions/31126596/saving-response-from-requests-to-file
https://pythonadventures.wordpress.com/2014/12/29/xml-to-dict-xml-to-json/
https://github.com/ThaWeatherman/scrapers/blob/master/boardgamegeek/get_game_info.py


COMPETITORS (use https://www.similarweb.com/ to test their numbers)
http://www.boardgamesfor.me/
https://boardgamegeek.com/wiki/page/Game_Recommendation_Algorithm
https://www.reddit.com/r/boardgames/comments/29wdng/announcing_the_new_board_game_recommendation_bot/
https://boardgamemenu.com/
http://stechschulte.net/2015/02/01/board-game-recommendations.html
http://meta.boardgames.stackexchange.com/questions/238/why-should-i-use-this-instead-of-boardgamegeek-whats-the-elevator-pitch


BGG
https://www.boardgamegeek.com/xmlapi
https://www.boardgamegeek.com/thread/99401/boardgamegeek-xml-api
https://boardgamegeek.com/wiki/page/Data_Mining
https://boardgamegeek.com/wiki/page/game_entry#
