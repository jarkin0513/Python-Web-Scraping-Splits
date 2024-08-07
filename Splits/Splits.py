from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains as AC
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

    # Pulls up specified URL and attempts to click 'Splits' button 
    def go_to_url(self):
        try:
            print(f"[INFO] Going to {paths.URL} . . .")

            self.get(paths.URL)
            WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, paths.BUTTON_SECTION))
            )
            print(f"[INFO] Pulled up {paths.URL}")

        except Exception as e_url:
            print(f"[ERROR] Failed to go to: {paths.URL}", e_url)

        try:
            print("[INFO] Clicking splits . . .")
            time.sleep(2)

            self.find_element(By.XPATH, paths.SPLITS_BUTTON_QUERY).click()
            print("[INFO] Clicked splits")

        except Exception as e_splits:
            print(f"[ERROR] Failed to click 'Splits' element", e_splits)

    def get_players(self):
        lst = self.get_team_stats()
        print(lst[1:])

    def get_team_stats(self):
        num_of_teams = self.get_num_teams() / 2

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
            print("[ERROR] Couldn't get team stats")
            return

        lst = [[]]
        for x in team_stats.splitlines():
            lst.append(x)
        lst.append("test")
        return lst
     

    # TODO - Could be used to check if players' stats meet criteria  
    def check_stats():
        pass

    # Finds unfavored team based on odds
    def get_underdog(self, away_path, home_path):
        print("[INFO] Getting underdog . . .")

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
    

    # Finds the number of teams to index through 
    def get_num_teams(self):
        number_of_teams = self.find_elements(By.CSS_SELECTOR, paths.NUM)
        print(f"[INFO] Number of available teams: {len(number_of_teams)}")
        return len(number_of_teams)
    
    def mutate_team_path(self):
        lst = [[]]
        num_of_teams = self.get_num_teams()
        if num_of_teams == 0:
            print("[ERROR] No teams found")

        # AWAY 1st row: //table[contains(@class,'table table-striped')]
        # HOME 1st row: (//table[contains(@class,'table table-striped')]/following::table)[2]
        temp_home_path = paths.HOME_TEAM_STATS
        temp_away_path = paths.AWAY_TEAM_STATS
        print(f"Temp home path: {temp_home_path}")
        print(f"Temp away path: {temp_away_path}")

        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, temp_home_path))
        )
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, temp_away_path))
        )
        team = self.get_underdog(temp_away_path, temp_home_path)
        if team[0] == '| Away':
            team_stats = self.find_element(By.XPATH, temp_away_path).text  
        elif team[0] == '| Home':
            team_stats = self.find_element(By.XPATH, temp_home_path).text
        else:
            print("[ERROR] Couldn't get team stats")
            return
        print(team)
        
        num_of_teams -= 1

        for x in team_stats.splitlines():
            lst.append(x)
        lst.append("test")
        print(lst)

        while num_of_teams != 0:

            for i in range(5, 70):
                try: 
                    temp_away_path = temp_home_path.replace(temp_home_path[67], str(i), 1)
                    
                    temp_home_path = temp_home_path.replace(temp_home_path[67], str(i + 2), 1)
                    print(f"Temp home path: {temp_home_path}")
                    print(f"Temp away path: {temp_away_path}")
                    print(f"i: {i}")
                    print(f"Number of teams: {num_of_teams}")

                    
                    while not WebDriverWait(self, 10).until(
                            EC.presence_of_element_located((By.XPATH, temp_home_path))
                        ):
                            self.execute_script("arguments[0].scrollIntoView();", self.find_element(By.XPATH, temp_home_path))
                            # element = self.find_element(By.XPATH, temp_home_path)
                        
                        # WebDriverWait(self, 1).until(
                        #     EC.presence_of_element_located((By.XPATH, temp_home_path))
                        # )
                    # WebDriverWait(self, 1).until(
                    #     EC.presence_of_element_located((By.XPATH, temp_away_path))
                    # )
                    time.sleep(2)

                    team = self.get_underdog(temp_away_path, temp_home_path)
                    if team[0] == '| Away':
                        team_stats = self.find_element(By.XPATH, temp_away_path).text  
                    elif team[0] == '| Home':
                        team_stats = self.find_element(By.XPATH, temp_home_path).text
                    else:
                        print("[ERROR] Couldn't get team stats")
                        return
                
                except Exception as e:
                    print(f"Error occurred: {e}")
                
            num_of_teams -= 1
            

            
            for x in team_stats.splitlines():
                lst.append(x)
            lst.append("test")
        return lst

    
    # TODO - Will be updated along the way
    def write_file(self):
        underdog_team = self.get_underdog()
        print(f"[INFO] Underdog team: {underdog_team}")
        for i in range(len(underdog_team)):
            f.write(str(underdog_team[i]))
            f.write(" | ")
        f.close()

    def test(self):
        team_names_span = self.find_elements(By.XPATH, "//span[@class='team-name']")
        team_odds_span = self.find_elements(By.XPATH, "//div[@class='odds']")
        for span in team_names_span:
            print(span.text)
        for span in team_odds_span:
            print(span.text)

        elements = self.find_elements(By.XPATH, paths.TEST1_X)
        actions = AC(self)
        for element in elements:
            actions.move_to_element(element).perform()
            element.click()
            time.sleep(2)

    