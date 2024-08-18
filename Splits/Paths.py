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