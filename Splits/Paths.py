URL = "https://www.fantasyalarm.com/mlb/lineups"

BUTTON_SECTION = "tool-btn-section"


HOME_TEAM_NAME = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title home-team-title']/div[@class='title push-right']/span[@class='team-name']"

HOME_TEAM_ODDS = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title home-team-title']/div[@class='odds']"

HOME_TEAM_TABLE = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='stat-section']/div[@class='table-wrapper x-scroll projected']/div[@class='overflow-container']/div/div/table[@class='table table-striped']"
# First player path: /tbody/tr[1]/td[3]
AWAY_TEAM_NAME = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title away-team-title']/div[@class='title']/span[@class='team-name']"

AWAY_TEAM_ODDS = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title away-team-title']/div[@class='odds push-right']"

AWAY_TEAM_TABLE = "/html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='stat-section']/div[@class='table-wrapper x-scroll projected mobile-hidden']/div[@class='overflow-container']/div/div/table[@class='table table-striped']/tbody/tr[1]/td[@class='text-center'][2]"

TEST = "body div.dialog-off-canvas-main-canvas[data-off-canvas-main-canvas=''] div.background.bg-white div.container div.no-gutters.page-content.row div#Main.bg-white.col.homepage.vue-layout div#lineup-app div.match-lineup-wrapper div.ssg-scm.ssg-scm-group-offers div div div.lineup-page-match div.stat-section div.mobile-hidden.projected.table-wrapper.x-scroll div.overflow-container div div table.table.table-striped tbody tr[index='0'][style='opacity: 1;'] td[index='2']"

AWAY_TEAM_STATS = "//table[contains(@class,'table table-striped')]"

HOME_TEAM_STATS = "(//table[contains(@class,'table table-striped')]/following::table)[2]"

# Number of total stat sections (Divide by 2 to only get underdogs)
NUM = "body div.dialog-off-canvas-main-canvas[data-off-canvas-main-canvas=''] div.background.bg-white div.container div.no-gutters.page-content.row div#Main.bg-white.col.homepage.vue-layout div#lineup-app div.match-lineup-wrapper div.ssg-scm.ssg-scm-group-offers div div div.lineup-page-match div.team-title-section"

# top_left = //table[contains(@class,'table table-striped')]
#             //table[contains(@class,'table table-striped')]
# top_right = (//table[contains(@class,'table table-striped')]/following::table)[2]
#             (//table[contains(@class,'table table-striped')]/following::table)[2]


# bottom_left = (//table[contains(@class,'table table-striped')]/following::table)[5]
#                 (//table[contains(@class,'table table-striped')]/following::table)[5]
# bottom_right = (//table[contains(@class,'table table-striped')]/following::table)[7]

# last_left = (//table[contains(@class,'table table-striped')]/following::table)[40]
#             //div[@id='lineup-app']/div[2]/div[1]/div[9]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/a[1]


AWAY_TEST_CSS = "div.lineup-page-match div.stat-section div.mobile-hidden.projected.table-wrapper.x-scroll div.overflow-container div div table.table.table-striped"
HOME_TEST_CSS = "div.stat-section div.projected.table-wrapper.x-scroll div.overflow-container div div table.table.table-striped"


# Home 2nd row: (//table[contains(@class,'table table-striped')]/following::table)[7]
# AWAY 2nd row: (//table[contains(@class,'table table-striped')]/following::table)[5]

# home 3rd row: (//table[contains(@class,'table table-striped')]/following::table)[12]
# away 3rd row: (//table[contains(@class,'table table-striped')]/following::table)[10]


TEST_XPATH = "//div[@id='lineup-app']/div[2]/div[1]/div[8]/div[1]/div[1]/div[2]/div[3]/a[1]"
SPLITS_BUTTONS_QUERY = "//a[@href='javascript:void(0)' and contains(@class, 'tabs-btn') and contains(text(), 'Splits')]"
# "//a[@href='javascript:void(0)' and @class='tabs-btn' and contains(text(), 'Splits')]"


# /html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[1]/div[1]/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title away-team-title']/div[@class='title']/span[@class='team-name']

# /html/body/div[@class='dialog-off-canvas-main-canvas']/div[@class='background bg-white']/div[@class='container']/div[@class='page-content row no-gutters']/div[@id='Main']/div[@id='lineup-app']/div[@class='match-lineup-wrapper']/div[@class='ssg-scm ssg-scm-group-offers']/div[2]/div/div[@class='lineup-page-match']/div[@class='team-title-section']/div[@class='team-title away-team-title']/div[@class='title']/span[@class='team-name']

AWAY_NAME_XPATH = "//span[@class='team-name']"
HOME_NAME_XPATH = "(//span[@class='team-name'])[2]"

#2nd row away     (//span[@class='team-name'])[3]

# //div[@id='lineup-app']/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]

# //div[@id='lineup-app']/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/div[2]/span[1]

TEAMS_NAME_SPAN = "//span[@class='team-name']"
HOME_TEAM_ODDS_SPAN = "//div[@class='odds']"
AWAY_TEAM_ODDS_SPAN = "//div[@class='odds push-right']"

# 
HOME_STATS_SPAN = "//div[@class='table-wrapper x-scroll confirmed']"
AWAY_STATS_SPAN = "//div[@class='table-wrapper x-scroll confirmed mlb mobile-hidden']"


# Team name example:                  "<span class='team-name'> Orioles</span>"
# Home stats are always contained in: "<div class='table-wrapper x-scroll confirmed'>"
# Away stats are always contained in: "<div class='table-wrapper x-scroll confirmed mlb mobile-hidden'>"
ALL_STATS_SPAN = "//table[contains(@class,'table table-striped')]"

# //table[contains(@class,'table table-striped')]

# text_list = [element.text for element in elements]

# # Join the texts into a single string, separated by commas
# combined_text = ", ".join(text_list)

# # If you want to split them again into a list (though it's the same as `text_list`)
# separated_list = combined_text.split(", ")

# # Output the results
# print(text_list)  # ['Text of element 1', 'Text of element 2']
# print(combined_text)  # 'Text of element 1, Text of element 2'
# print(separated_list)  # ['Text of element 1', 'Text of element 2']

TEST_STATS = stats = [[ ['# POS NAME AB H HR RBI AVG\n1 2B Maikel Garcia (R) 0 0 0 0 .000\n2 SS Bobby Witt (R) 0 0 0 0 .000\n3 DH Vinnie Pasquantino (L) 0 0 0 0 .000\n4 1B Salvador Perez (R) 0 0 0 0 .000\n5 RF Hunter Renfroe (R) 6 1 1 1 .167\n6 C Freddy Fermin (R) 0 0 0 0 .000\n7 CF Garrett Hampson (R) 1 1 0 0 1.000\n8 3B Paul DeJong (R) 2 0 0 0 .000\n9 LF Dairon Blanco (R) 0 0 0 0 .000'], 
['# POS NAME AB H HR RBI AVG\n1 2B Jonathan India (R) 5 0 0 0 .000\n2 SS Elly De La Cruz (B) 2 0 0 0 .000\n3 C Tyler Stephenson (R) 3 0 0 0 .000\n4 CF TJ Friedl (L) 6 1 0 0 .167\n5 LF Spencer Steer (R) 5 0 0 0 .000\n6 1B Jeimer Candelario (B) 3 0 0 0 .000\n7 DH Ty France (R) 18 9 0 2 .500\n8 RF Jake Fraley (L) 7 5 0 2 .714\n9 3B Noelvi Marte (R) 0 0 0 0 .000']], 

[ 
['# POS NAME AB H R HR RBI SB\n1 SS Willi Castro (B) 3 1 0 0 0 0\n2 LF Trevor Larnach (L) 3 1 1 1 1 0\n3 3B Royce Lewis (R) 3 1 0 0 0 0\n4 DH Matt Wallner (L) 3 0 0 0 0 0\n5 1B Carlos Santana (B) 3 0 0 0 0 0\n6 RF Max Kepler (L) 3 0 0 0 0 0\n7 2B Edouard Julien (L) 2 0 0 0 0 0\n8 C Christian Vázquez (R) 2 0 0 0 0 0\n9 CF Austin Martin (R) 2 0 0 0 0 0'], 
['# POS NAME AB H R HR RBI SB\n1 2B Marcus Semien (R) 3 1 0 0 0 0\n2 SS Corey Seager (L) 3 1 0 0 0 0\n3 1B Nathaniel Lowe (L) 3 0 0 0 0 0\n4 RF Adolis García (R) 3 0 0 0 0 0\n5 LF Wyatt Langford (R) 3 1 1 0 0 0\n6 3B Josh Jung (R) 3 1 0 0 0 0\n7 C Jonah Heim (B) 3 1 1 0 0 0\n8 DH Carson Kelly (R) 3 2 0 0 2 0\n9 CF Leody Taveras (B) 2 0 0 0 0 0']
], 

[
['# POS NAME AB H R HR RBI SB\n1 SS Tyler Fitzgerald (R) 2 0 0 0 0 0\n2 1B LaMonte Wade (L) 3 0 0 0 0 0\n3 LF Heliot Ramos (R) 3 0 0 0 0 0\n4 DH Michael Conforto (L) 3 0 0 0 0 0\n5 3B Matt Chapman (R) 2 0 0 0 0 0\n6 RF Mike Yastrzemski (L) 1 0 0 0 0 0\n7 C Patrick Bailey (B) 2 0 0 0 0 0\n8 2B Brett Wisely (L) 2 0 0 0 0 0\n9 CF Grant McCray (L) 2 1 0 0 0 0'], 
['# POS NAME AB H R HR RBI SB\n1 RF Lawrence Butler (L) 2 0 0 0 1 0\n2 DH Brent Rooker (R) 3 0 0 0 0 0\n3 CF JJ Bleday (L) 2 0 0 0 0 0\n4 LF Miguel Andujar (R) 3 1 1 0 0 0\n5 C Shea Langeliers (R) 3 0 0 0 0 0\n6 1B Seth Brown (L) 3 3 0 0 1 0\n7 2B Zack Gelof (R) 3 1 1 0 0 0\n8 3B Darell Hernaiz (R) 1 0 0 0 0 0\n9 SS Max Schuemann (R) 1 0 0 0 0 0']], [['# POS NAME AB H R HR RBI SB\n1 SS Nicky Lopez (L) 3 0 0 0 0 0\n2 CF Luis Robert (R) 3 1 0 0 0 0\n3 LF Andrew Benintendi (L) 1 0 1 0 0 1\n4 1B Andrew Vaughn (R) 3 1 0 0 0 0\n5 DH Gavin Sheets (L) 2 2 0 0 1 0\n6 3B Lenyn Sosa (R) 2 0 0 0 0 0\n7 RF Dominic Fletcher (L) 2 0 0 0 0 0\n8 C Chuckie Robinson (R) 2 0 0 0 0 0\n9 2B Brooks Baldwin (B) 2 0 0 0 0 0'], ['# POS NAME AB H R HR RBI SB\n1 2B Jose Altuve (R) 3 1 1 0 2 1\n2 LF Yordan Alvarez (L) 3 1 0 0 1 0\n3 C Yainer Diaz (R) 3 1 0 0 0 0\n4 SS Jeremy Peña (R) 3 0 0 0 0 1\n5 1B Jon Singleton (L) 3 0 0 0 0 0\n6 DH Victor Caratini (B) 3 2 1 0 0 0\n7 CF Jake Meyers (R) 2 1 0 0 0 0\n8 3B Shay Whitcomb (R) 1 1 1 0 0 0\n9 RF Mauricio Dubón (R) 1 1 1 0 1 0']]]