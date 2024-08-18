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

    # Pulls up specified URL and attempts to click 'Splits' buttons
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

        time.sleep(2)

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

        print(underdogs_output)
        # print(len(underdogs_output))

        print("[INFO] Got underdogs")
        return underdogs_output
    

    # Finds the number of teams to index through 
    def get_num_games(self):
        number_of_teams = self.find_elements(By.CSS_SELECTOR, paths.NUM)
        print(f"[INFO] Number of available games: {len(number_of_teams)}")
        return len(number_of_teams)
    
    
    # TODO - Will be updated along the way
    def write_file(self):
        underdog_team = self.get_underdog()
        print(f"[INFO] Underdog team: {underdog_team}")
        for i in range(len(underdog_team)):
            f.write(str(underdog_team[i]))
            f.write(" | ")
        f.close()

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
            print("[ERROR] Number of teams does not match sum of home and away odds")
            return

        for i in range(len(home_team_odds)): 
            if self.is_castable_to_int(home_team_odds[i]) and self.is_castable_to_int(away_team_odds[i]):
                home_team = ["Home", team_names[2 * i + 1], home_team_odds[i], i]
                away_team = ["Away", team_names[2 * i], away_team_odds[i], i]
                team_pairs.append([home_team, away_team])
            else:
                print(f"[WARNING] Team(s) in game {i + 1} does not have odds listed (Ignoring)")

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
            print(f"pairs count: {pairs_count}")
            print(f"num games: {num_games}")
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
        for pair in stats_span:
            print(f"{pair}\n")
        return stats_span
    
    def get_underdog_team_stats(self):
        # actions = AC(self)
        # actions.scroll_by_amount(0, 1000).perform()
        # time.sleep(2)

        underdogs = self.get_underdogs()
        # print(underdogs)

        stats = self.get_stats_span()
        # for pair in stats:
        #     print(f"{pair} \n")
            
        # print(stats[0])
        # print(len(stats))

        team_stats = []

        for i, team_pair in enumerate(stats):
            # print(i)
            # print(team_pair)
            if len(team_pair) < 2:
                continue

        #     # print(team_pair)

            away_stat = team_pair[0]
            home_stat = team_pair[1]

        #     # if i + 1 < len(stats):
        #     #     home_stat = stats[i + 1]
        #     #     away_stat = stats[i]

            for team in underdogs:
                if team[0] == '| Home':
                    home_final = [team[1], home_stat]
                    team_stats.append(home_final)
                elif team[0] == '| Away':
                    away_final = [team[1], away_stat[i][0]]
                    team_stats.append(away_final)
        
        print(team_stats)

        # for i in range(0, len(stats)):
        #     for team in underdogs:
        #         if team[0] == '| Home':
        #             home_final = [team[1], stats[i][1]]
        #             team_stats.append(home_final)
        #         elif team[0] == '| Away':
        #             away_final = [team[1], stats[i][0]]
        #             team_stats.append(away_final)

        # print(team_stats)

        player_stats = []

        for team in team_stats:
            team_name = team[0]
            player_data = team[1]

            team_player_stats = []

            for stats_string in player_data:
                player_lines = stats_string.split('\n')

                for line in player_lines:
                    if line.strip() and not line.startswith("#"):
                        parts = line.split()
                        player_name = " ".join(parts[1:-5])
                        ab = parts[-5]
                        hr = parts[-3]
                        avg = parts[-1]

                        team_player_stats.append({
                            'Player': player_name,
                            'AB': ab,
                            'HR': hr,
                            'AVG': avg
                        })

                        # # Check for duplicates
                        # if not any(player['Player'] == player_name for player in team_player_stats):
                        #     team_player_stats.append({
                        #         'Player': player_name,
                        #         'AB': ab,
                        #         'HR': hr,
                        #         'AVG': avg
                        #     })
            unique_players = {}
            for player in team_player_stats:
                unique_players[player['Player']] = player

            player_stats.append({
                'Team': team_name,
                'Players': list(unique_players.values())      #team_player_stats
            })

        # print(player_stats)
        print("\n\n")
        return player_stats
    
    def get_underdog_team_stats1(self):
        underdogs = self.get_underdogs()
        # print(underdogs)
        stats = self.get_stats_span()
        print(stats)
        print(len(stats[0]))

        team_stats = []

        for team in underdogs:

            away_stat = team_pair[0]
            home_stat = team_pair[1]

            for team in underdogs:
                if team[0] == '| Home':
                    home_final = [team[1], home_stat]
                    team_stats.append(home_final)
                elif team[0] == '| Away':
                    away_final = [team[1], away_stat[i][0]]
                    team_stats.append(away_final)
        
        print(team_stats)

        player_stats = []

        for team in team_stats:
            team_name = team[0]
            player_data = team[1]

            team_player_stats = []

            for stats_string in player_data:
                player_lines = stats_string.split('\n')

                for line in player_lines:
                    if line.strip() and not line.startswith("#"):
                        parts = line.split()
                        player_name = " ".join(parts[1:-5])
                        ab = parts[-5]
                        hr = parts[-3]
                        avg = parts[-1]

                        team_player_stats.append({
                            'Player': player_name,
                            'AB': ab,
                            'HR': hr,
                            'AVG': avg
                        })

                        # # Check for duplicates
                        # if not any(player['Player'] == player_name for player in team_player_stats):
                        #     team_player_stats.append({
                        #         'Player': player_name,
                        #         'AB': ab,
                        #         'HR': hr,
                        #         'AVG': avg
                        #     })
            unique_players = {}
            for player in team_player_stats:
                unique_players[player['Player']] = player

            player_stats.append({
                'Team': team_name,
                'Players': list(unique_players.values())      #team_player_stats
            })

        # print(player_stats)
        print("\n\n")
        return player_stats
    
    def get_final_players(self, threshold_ab, threshold_hr, threshold_avg):
        # player_stats = [{'Team': 'Pirates', 'Players': [{'Player': 'Jose Asuna ()', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Ji Hwan Bae (L)', 'AB': '1', 'HR': '0', 'AVG': '.000'}, {'Player': 'Joey Bart (R)', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Jack Brannigan ()', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Oneil Cruz (L)', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Bryan De La Cruz (R)', 'AB': '6', 'HR': '0', 'AVG': '.167'}, {'Player': 'Yasmani Grandal (B)', 'AB': '16', 'HR': '2', 'AVG': '.375'}, {'Player': "Ke'Bryan Hayes (R)", 'AB': '9', 'HR': '0', 'AVG': '.222'}, {'Player': 'Connor Joe (R)', 'AB': '5', 'HR': '0', 'AVG': '.400'}, {'Player': 'Isiah Kiner-Falefa (R)', 'AB': '8', 'HR': '0', 'AVG': '.375'}, {'Player': 'Grant Koch (R)', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Andrew McCutchen (R)', 'AB': '11', 'HR': '0', 'AVG': '.091'}, {'Player': 'Bryan Reynolds (B)', 'AB': '11', 'HR': '0', 'AVG': '.000'}, {'Player': 'Michael A. Taylor (R)', 'AB': '3', 'HR': '1', 'AVG': '.333'}, {'Player': 'Rowdy Tellez (L)', 'AB': '6', 'HR': '0', 'AVG': '.167'}, {'Player': 'Jared Triolo (R)', 'AB': '0', 'HR': '0', 'AVG': '.000'}]}, {'Team': 'Tigers', 'Players': [{'Player': 'Jose Asuna ()', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Ji Hwan Bae (L)', 'AB': '1', 'HR': '0', 'AVG': '.000'}, {'Player': 'Joey Bart (R)', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Jack Brannigan ()', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Oneil Cruz (L)', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Bryan De La Cruz (R)', 'AB': '6', 'HR': '0', 'AVG': '.167'}, {'Player': 'Yasmani Grandal (B)', 'AB': '16', 'HR': '2', 'AVG': '.375'}, {'Player': "Ke'Bryan Hayes (R)", 'AB': '9', 'HR': '0', 'AVG': '.222'}, {'Player': 'Connor Joe (R)', 'AB': '5', 'HR': '0', 'AVG': '.400'}, {'Player': 'Isiah Kiner-Falefa (R)', 'AB': '8', 'HR': '0', 'AVG': '.375'}, {'Player': 'Grant Koch (R)', 'AB': '0', 'HR': '0', 'AVG': '.000'}, {'Player': 'Andrew McCutchen (R)', 'AB': '11', 'HR': '0', 'AVG': '.091'}, {'Player': 'Bryan Reynolds (B)', 'AB': '11', 'HR': '0', 'AVG': '.000'}, {'Player': 'Michael A. Taylor (R)', 'AB': '3', 'HR': '1', 'AVG': '.333'}, {'Player': 'Rowdy Tellez (L)', 'AB': '6', 'HR': '0', 'AVG': '.167'}, {'Player': 'Jared Triolo (R)', 'AB': '0', 'HR': '0', 'AVG': '.000'}]}]
        player_stats = self.get_underdog_team_stats()
        # print(player_stats)
        print("\n\n")

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

        print(list(players_meeting_threshold)[:100])
        return list(players_meeting_threshold)

    
    def test(self):
        print("In test")
        stats_span = []
        # stats = self.find_elements(By.XPATH, paths.ALL_STATS_SPAN)
        stats = WebDriverWait(self, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, paths.ALL_STATS_SPAN))
        )

        for i, element in enumerate(stats):
            print(f"Element {i}: Type={type(element)}, Text={getattr(element, 'text', 'No text attribute')}")


        for element in stats:
            stats_span.append([element.text])
        
        print(stats_span)


    def scroll_collect_elements(self):
        num_games = self.get_num_games()
        all_table_elements = []
        seen_positions = set()

        prev_height = self.execute_script("return document.body.scrollHeight")

        print("[INFO] Clicking splits . . .")
        while True:
            self.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            # time.sleep(2)

            buttons = self.find_elements(By.XPATH, paths.SPLITS_BUTTONS_QUERY)
            actions = AC(self)
            for button in buttons:
                try:
                    actions.move_to_element(button).perform()
                    button.click()
                    time.sleep(1)

                    table_elements = self.find_elements(By.XPATH, paths.ALL_STATS_SPAN)
                    for table in table_elements:
                        table_position = tuple(table.location.values())
                        if table.text not in all_table_elements and table_position not in seen_positions:
                            all_table_elements.append(table.text)
                            seen_positions.add(table_position)
                            

                except Exception as e:
                    print(f"Error interacting with button: {e}")

            #   Check the new scroll height after scrolling
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == prev_height:
                break  # Exit the loop if the scroll height hasn't changed, meaning no more content is loading
            prev_height = new_height  

        print("[INFO] Clicked splits") 

        # print(all_table_elements)
        # print(len(all_table_elements))
        # for element in table_elements:
        #     print(element.text)
        # print(f"Collected {len(all_table_elements)} elements")
        return all_table_elements
    
    