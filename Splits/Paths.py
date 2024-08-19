URL = "https://www.fantasyalarm.com/mlb/lineups"

BUTTON_SECTION = "tool-btn-section"

HOME_TEAM_ODDS = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title home-team-title']/div[@class='odds']"

AWAY_TEAM_ODDS = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title away-team-title']/div[@class='odds push-right']"

NUM = "body div.dialog-off-canvas-main-canvas[data-off-canvas-main-canvas=''] div.background.bg-white div.container div.no-gutters.page-content.row div#Main.bg-white.col.homepage.vue-layout div#lineup-app div.match-lineup-wrapper div.ssg-scm.ssg-scm-group-offers div div div.lineup-page-match div.team-title-section"

SPLITS_BUTTONS_QUERY = "//a[@href='javascript:void(0)' and contains(@class, 'tabs-btn') and contains(text(), 'Splits')]"

TEAMS_NAME_SPAN = "//span[@class='team-name']"

HOME_TEAM_ODDS_SPAN = "//div[@class='odds']"

AWAY_TEAM_ODDS_SPAN = "//div[@class='odds push-right']"

ALL_STATS_SPAN = "//table[contains(@class,'table table-striped')]"

TEST_STATS = [
[ 
['# POS NAME AB H HR RBI AVG\n1 2B Maikel Garcia (R) 1 2 3 4 .000\n2 SS Bobby Witt (R) 0 0 0 0 .000\n3 DH Vinnie Pasquantino (L) 0 0 0 0 .000\n4 1B Salvador Perez (R) 0 0 0 0 .000\n5 RF Hunter Renfroe (R) 6 1 1 1 .167\n6 C Freddy Fermin (R) 0 0 0 0 .000\n7 CF Garrett Hampson (R) 1 1 0 0 1.000\n8 3B Paul DeJong (R) 2 0 0 0 .000\n9 LF Dairon Blanco (R) 0 0 0 0 .000'], 
['# POS NAME AB H HR RBI AVG\n1 2B Jonathan India (R) 5 0 0 0 .000\n2 SS Elly De La Cruz (B) 2 0 0 0 .000\n3 C Tyler Stephenson (R) 3 0 0 0 .000\n4 CF TJ Friedl (L) 6 1 0 0 .167\n5 LF Spencer Steer (R) 5 0 0 0 .000\n6 1B Jeimer Candelario (B) 3 0 0 0 .000\n7 DH Ty France (R) 18 9 0 2 .500\n8 RF Jake Fraley (L) 7 5 0 2 .714\n9 3B Noelvi Marte (R) 0 0 0 0 .000']
], 

[ 
['# POS NAME AB H R HR RBI SB\n1 SS Willi Castro (B) 3 1 0 0 .0\n2 LF Trevor Larnach (L) 3 1 1 1 .1\n3 3B Royce Lewis (R) 3 1 0 0 .0\n4 DH Matt Wallner (L) 3 0 0 0 .1\n5 1B Carlos Santana (B) 3 0 0 0 .0\n6 RF Max Kepler (L) 3 0 0 0 .0\n7 2B Edouard Julien (L) 2 0 0 0 0 0\n8 C Christian Vázquez (R) 2 0 0 0 0 0\n9 CF Austin Martin (R) 2 0 0 0 0 0'], 
['# POS NAME AB H R HR RBI SB\n1 2B Marcus Semien (R) 3 1 0 0 0 0\n2 SS Corey Seager (L) 3 1 0 0 0 0\n']
], 

[
['# POS NAME AB H R HR RBI SB\n1 SS Tyler Fitzgerald (R) 2 0 0 0 .1\n2 1B LaMonte Wade (L) 3 0 0 0 .0\n3 LF Heliot Ramos (R) 3 0 0 0 .0\n4 DH Michael Conforto (L) 3 0 0 0 0 .0\n'], 
['# POS NAME AB H R HR RBI SB\n1 RF Lawrence Butler (L) 2 0 0 0 .1\n2 DH Brent Rooker (R) 3 0 0 0 .0\n3 CF JJ Bleday (L) 2 0 0 0 .0\n4 LF Miguel Andujar (R) 3 1 1 0 .1\n']
]

]

TEST_UNDERDOGS = [
['| Away', 'Royals', '113', 0], 
['| Away', 'Twins', '103', 1], 
['| Home', 'Athletics', '113', 2]
 
]