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
from progress.bar import Bar
import Splits.Paths as paths


f = open("output.txt", "w")

class Splits(webdriver.Chrome):

    def __init__(self, driver_path="chromedriver.exe", chrome_options=Options(), teardown=False):
        self.driver_path = driver_path        
        self.chrome_options = chrome_options
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless=new')
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.teardown = teardown
        super(Splits, self).__init__(options=chrome_options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # Pulls up specified URL and attempts to click 'Splits' buttons
    def go_to_url(self):
        try:
            print(f"[INFO] Going to {paths.URL} . . .")

            self.get(paths.URL)
            WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, paths.BUTTON_SECTION))
            )
            print(f"[INFO] Pulled up {paths.URL}")
            time.sleep(2)
            return True

        except Exception as e_url:
            print(f"\033[91m[ERROR] Failed to go to: {paths.URL}\033[0m", e_url)
            return False

        

    # Finds unfavored team based on odds
    def get_underdogs(self):
        print("[INFO] Getting underdogs . . .")

        team_pairs = self.get_team_pairs()
        underdogs_output = []

        for i in range(len(team_pairs)):
            lst = []
            if int(team_pairs[i][0][2]) > int(team_pairs[i][1][2]):
                underdog_name = team_pairs[i][0][1]
                underdog_odds = team_pairs[i][0][2] 
                game_index = team_pairs[i][0][3]
                lst = ['| Home', underdog_name, underdog_odds, game_index]
                underdogs_output.append(lst)

            else:
                underdog_name = team_pairs[i][1][1]
                underdog_odds = team_pairs[i][1][2] 
                game_index = team_pairs[i][1][3]
                lst = ['| Away', underdog_name, underdog_odds, game_index]
                underdogs_output.append(lst)

        print("[INFO] Underdogs:")
        print(underdogs_output)
        # print(len(underdogs_output))

        print("[INFO] Got underdogs")
        return underdogs_output
    

    # Finds the number of teams to index through 
    def get_num_games(self):
        number_of_teams = self.find_elements(By.CSS_SELECTOR, paths.NUM)
        return len(number_of_teams)
    

    def get_team_pairs(self):
        print("[INFO] Grabbing team pairs . . .")
        team_pairs = []

        team_names_span = self.find_elements(By.XPATH, paths.TEAMS_NAME_SPAN)
        home_team_odds_span = self.find_elements(By.XPATH, paths.HOME_TEAM_ODDS_SPAN)
        away_team_odds_span = self.find_elements(By.XPATH, paths.AWAY_TEAM_ODDS_SPAN)

        team_names = [span.text for span in team_names_span]
        home_team_odds = [span.text for span in home_team_odds_span]
        away_team_odds = [span.text for span in away_team_odds_span]

        if len(team_names) != (len(home_team_odds) + len(away_team_odds)):
            print("\033[91m[ERROR] Number of teams does not match sum of home and away odds\033[0m")
            return

        for i in range(len(home_team_odds)): 
            if self.is_castable_to_int(home_team_odds[i]) and self.is_castable_to_int(away_team_odds[i]):
                home_team = ["Home", team_names[2 * i + 1], home_team_odds[i], i]
                away_team = ["Away", team_names[2 * i], away_team_odds[i], i]
                team_pairs.append([home_team, away_team])
            else:
                print(f"\033[93m[WARNING] Team(s) in game {i + 1} does not have odds listed (Ignoring)\033[0m")

        print("[INFO] Grabbed team pairs")
        # print(team_pairs)
        return team_pairs
    
    def is_castable_to_int(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

            
    def get_stats_span(self):
        print("[INFO] Getting stats span . . .")
        stats_span = []
        stats = self.scroll_collect_elements()
        num_games = self.get_num_games()
        pairs_count = 0

        # Filter out pitchers
        unwanted_keywords = ['OPP PITCHER', 'IP HA ER BB K W']
        filtered_stats = []

        try:
            filtered_stats = [element for element in stats if not any(keyword in element for keyword in unwanted_keywords)]
        except Exception as e:
            print(f"Error occured: {e}")

        # for i in range(len(filtered_stats)):
        #     print(filtered_stats[i])

        for i in range(0, len(filtered_stats), 2):
            if pairs_count >= num_games:
                break

            team_pair = []
            if i < len(filtered_stats):
                away_team = filtered_stats[i]
                team_pair.append([away_team])
            if i + 1 < len(filtered_stats):
                home_team = filtered_stats[i + 1]
                team_pair.append([home_team])

            stats_span.append(team_pair)
            pairs_count += 1

        
        # print(stats_span)
        # print(len(stats_span))
        print("[INFO] Got stats span")
        # for pair in stats_span:
        #     print(f"{pair}\n")
        return stats_span
    
    def get_underdog_team_stats(self):
        underdogs = self.get_underdogs()
        stats = self.get_stats_span()
        # underdogs = paths.TEST_UNDERDOGS
        # stats = paths.TEST_STATS
        # for pair in stats:
        #     print(f"{pair} \n")

        team_stats = []

        for i in range(len(stats)):
            if underdogs[i][0] == '| Home':
                team_stats.append([underdogs[i][1], stats[i][1]])
                # print(f"{stats[i][1]} \n")
            elif underdogs[i][0] == '| Away':
                team_stats.append([underdogs[i][1], stats[i][0]])
                # print(f"{stats[i][0]} \n")
        # print(len(team_stats))

        player_stats = []

        for i in range(len(team_stats)):
            # print(i)
            team_name = team_stats[i][0]
            player_data = team_stats[i][1]
            # print(f"Team: {team_name} Player Data: {player_data}")

            team_player_stats = {
                'Team': team_name,
                'Players': []
            }

            for stats_string in player_data:
                player_lines = stats_string.split('\n')

                for line in player_lines:
                    # print(line)
                    if line.strip() and not line.startswith("#"):
                        parts = line.split()
                        player_name = " ".join(parts[1:-5])
                        ab = parts[-5]
                        hr = parts[-3]
                        avg = parts[-1]

                        # # Check for duplicates
                        if not any(player['Player'] == player_name for player in team_player_stats['Players']):
                            team_player_stats['Players'].append({
                                'Player': player_name,
                                'AB': ab,
                                'HR': hr,
                                'AVG': avg
                            })

            player_stats.append(team_player_stats)

        # print("\n\n")
        # print(player_stats)
        return player_stats
    
    
    def get_final_players(self, threshold_ab, threshold_hr, threshold_avg):
        player_stats = self.get_underdog_team_stats()
        # print(player_stats)
        # print("\n\n")

        players_meeting_threshold = set() # Avoid duplicates

        for team in player_stats:
            team_name = team['Team']
            stats = team['Players']
            # print(f"Team: {team_name}")
            for player in stats:
                try:
                    # print(f"Player: {player['Player']}")
                    ab = int(player['AB'])
                    hr = int(player['HR'])
                    avg = float(player['AVG'])

                    if ab >= threshold_ab and hr < threshold_hr and avg <= threshold_avg:
                        players_meeting_threshold.add(
                            (team_name, player['Player'])
                        )

                except ValueError as e:
                    print(f"Eror processing player data: {e}, player info: {player}")

        # print(list(players_meeting_threshold))
        return list(players_meeting_threshold)

    def scroll_collect_elements(self):
        num_games = self.get_num_games()
        count = 0
        all_table_elements = []

        print(f"[INFO] Number of available games: {num_games}")

        bar = Bar('[INFO] Collecting information', max = num_games)

        prev_height = self.execute_script("return document.body.scrollHeight")

        while count < num_games:
            self.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            buttons = self.find_elements(By.XPATH, paths.SPLITS_BUTTONS_QUERY)
            actions = AC(self)
            for button in buttons:
                try:
                    actions.move_to_element(button).perform()
                    if button.text == 'Splits' and 'active' not in button.get_attribute("class"):
                        button.click()
                        time.sleep(1)

                    count += 1
                    bar.next()

                except Exception as e:
                    print(f"Error interacting with button: {e}")

            table_elements = self.find_elements(By.XPATH, paths.ALL_STATS_SPAN)
            for table in table_elements:
                all_table_elements.append(table.text)
            

            #   Check the new scroll height after scrolling
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == prev_height:
                break  # Exit the loop if the scroll height hasn't changed, meaning no more content is loading
            prev_height = new_height  

        bar.finish()
        print("[INFO] Finished getting info") 

        # print(all_table_elements)
        # print(len(all_table_elements))
        # for element in table_elements:
        #     print(element.text)
        # print(f"Collected {len(all_table_elements)} elements")
        return all_table_elements