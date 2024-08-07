from Splits.Splits import Splits
import time

def main() -> int:
    try:
        with Splits() as bot:
            bot.go_to_url()
            bot.test()
            # bot.get_num_teams()
            # bot.write_file()
            # bot.get_players()
            # bot.mutate_team_path()
            

            time.sleep(2)

            # bot.teardown = True
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1



if __name__ == '__main__':
    print("\nExit code ", main())