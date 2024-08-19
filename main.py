from Splits.Splits import Splits
from Splits.FileWriter import FileWriter
import sys

def main() -> int:

    args = sys.argv
    if(len(sys.argv) == 4):
        ab_threshold = int(args[1])
        hr_threshold = int(args[2])
        avg_threshold = float(args[3])
    elif(len(sys.argv) == 1):
        ab_threshold = 5 # 5, 1
        hr_threshold = 0 # 0, 1
        avg_threshold = .200 # .200, .300
    else:
        print(f"[ERROR] Invalid number of arguments")
        return -2
    
    try:
        with Splits() as bot:
            bot.go_to_url()

            final_players = bot.get_final_players(ab_threshold, hr_threshold, avg_threshold)

            file_writer = FileWriter("output.txt")

            file_writer.write_results(final_players, ab_threshold, hr_threshold, avg_threshold)
            
            # bot.teardown = True

        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1


if __name__ == '__main__':
    print("\nExit code ", main())