from Splits.Splits import Splits
from Splits.FileWriter import FileWriter
import time

def main() -> int:
    ab_threshold = 1 # 5
    hr_threshold = 1 # 0 
    avg_threshold = .300 # .200
    
    try:
        with Splits() as bot:
            bot.go_to_url()
            # bot.get_team_pairs()
            # bot.get_underdogs()
            # bot.get_num_teams()
            # bot.write_file()
            # bot.get_players()
            # bot.mutate_team_path()
            # bot.get_stats_span()
            # bot.scroll_collect_elements()
            
            # bot.get_underdog_team_stats()

            final_players = bot.get_final_players(ab_threshold, hr_threshold, avg_threshold)

            file_writer = FileWriter("output.txt")

            file_writer.write_results(final_players, ab_threshold, hr_threshold, avg_threshold)
            
            bot.teardown = True

        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1



if __name__ == '__main__':
    print("\nExit code ", main())