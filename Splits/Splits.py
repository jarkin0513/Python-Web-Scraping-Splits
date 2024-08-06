from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import Splits.Paths as paths


f = open("output.txt", "w")

class Splits(webdriver.Chrome):

    def __init__(self, driver_path="chromedriver.exe", chrome_options=Options(), teardown=False):
        self.driver_path = driver_path        
        self.chrome_options = chrome_options
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.teardown = teardown
        super(Splits, self).__init__(options=chrome_options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def go_to_url(self):
        print(f"Going to {paths.URL} . . .")

        self.get(paths.URL)
        WebDriverWait(self, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, paths.BUTTON_SECTION))
        )
        print(f"Pulled up {paths.URL}")

        print("Clicking splits . . .")
        time.sleep(2)

        self.find_element(By.XPATH, paths.SPLITS_BUTTON_QUERY).click()
        print("Clicked splits")

    def get_players(self):
        lst = self.get_team_stats()
        print(lst[1:])

    def get_team_stats(self):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, paths.HOME_TEAM_STATS))
        )
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, paths.AWAY_TEAM_STATS))
        )
        time.sleep(2)

        team = self.get_underdog()
        if team[0] == '| Away':
            team_stats = self.find_element(By.XPATH, paths.AWAY_TEAM_STATS).text  
        elif team[0] == '| Home':
            team_stats = self.find_element(By.XPATH, paths.HOME_TEAM_STATS).text
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

    # Finds unfavored team based on odds
    def get_underdog(self):
        print("Getting underdog . . .")

        underdog_output = []

        home_team_name = self.find_element(By.XPATH, paths.HOME_TEAM_NAME).text
        home_team_odds = int(self.find_element(By.XPATH, paths.HOME_TEAM_ODDS).text)

        away_team_name = self.find_element(By.XPATH, paths.AWAY_TEAM_NAME).text
        away_team_odds = int(self.find_element(By.XPATH, paths.AWAY_TEAM_ODDS).text)

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
    
    # TODO - Will be updated along the way
    def write_file(self):
        underdog_team = self.get_underdog()
        print(f"Underdog team: {underdog_team}")
        for i in range(len(underdog_team)):
            f.write(str(underdog_team[i]))
            f.write(" | ")
        f.close()


    