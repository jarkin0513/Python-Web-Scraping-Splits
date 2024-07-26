URL = "https://www.fantasyalarm.com/mlb/lineups"

BUTTON_SECTION = "tool-btn-section"

SPLITS_BUTTON_QUERY = "//div[@id='lineup-app']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]"

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
TEST = "body div.dialog-off-canvas-main-canvas[data-off-canvas-main-canvas=''] div.background.bg-white div.container div.no-gutters.page-content.row div#Main.bg-white.col.homepage.vue-layout div#lineup-app div.match-lineup-wrapper div.ssg-scm.ssg-scm-group-offers div div div.lineup-page-match div.team-title-section"