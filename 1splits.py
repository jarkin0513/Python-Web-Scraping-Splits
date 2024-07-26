from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import io
import time
import Splits.paths 

# Needs to have <= .200 AVG, => 5 AB, and 0 HR 
# No players from favored teams (could maybe be optional)

players = {}

f = open("output.txt", "w")

EXE_PATH = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options, service=EXE_PATH)
driver.get("https://www.fantasyalarm.com/mlb/lineups")

# cookie = {'name' : 'foo', 'value' : 'bar'}
# print(driver.get_cookie("foo"))

def main():
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, paths.BUTTON_SECTION))
    )

    time.sleep(2)

    driver.find_element(By.XPATH, paths.SPLITS_BUTTON_QUERY).click()
    print("Clicked splits")

    underdog_team = get_underdog()
    print(f"Underdog team: {underdog_team}")
    for i in range(len(underdog_team)):
        f.write(str(underdog_team[i]))
        f.write(" | ")
    f.close()

    num = driver.find_elements(By.CSS_SELECTOR, paths.TEST)
    print(len(num))
    
    get_players()

    time.sleep(30)

    driver.close()

# TODO - Will need to get each section for each team on page. Comb through the list and check if player stats meet criteria. Add player name and a True/False value for each depending if they meet criteria or not
def get_players():
    lst = get_team_stats()
    print(lst[1:])

# TODO - Maybe unneccessary. Could be used to get each container that holds each team's stats 
def get_team_stats():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, paths.HOME_TEAM_STATS))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, paths.AWAY_TEAM_STATS))
    )
    time.sleep(2)

    team = get_underdog()
    if team[0] == '| Away':
        team_stats = driver.find_element(By.XPATH, paths.AWAY_TEAM_STATS).text  
    elif team[0] == '| Home':
        team_stats = driver.find_element(By.XPATH, paths.HOME_TEAM_STATS).text
    else:
        print("Couldn't get team stats")
        return
    
    lst = []
    for x in team_stats.splitlines():
        lst.append(x)
    return lst
     

# TODO - Could be used to check if players' stats meet criteria  
def check_stats():
    pass

def get_underdog():

    underdog_output = []

    home_team_name = driver.find_element(By.XPATH, paths.HOME_TEAM_NAME).text
    home_team_odds = int(driver.find_element(By.XPATH, paths.HOME_TEAM_ODDS).text)

    away_team_name = driver.find_element(By.XPATH, paths.AWAY_TEAM_NAME).text
    away_team_odds = int(driver.find_element(By.XPATH, paths.AWAY_TEAM_ODDS).text)

    underdog_output.append('| Home')
    underdog_name = home_team_name
    underdog_odds = home_team_odds
    if away_team_odds < home_team_odds:
        underdog_output[0] = '| Away'
        underdog_name = away_team_name
        underdog_odds = away_team_odds

    underdog_output.append(underdog_name)
    underdog_output.append(underdog_odds)

    return underdog_output

if __name__ == '__main__':
    main()
