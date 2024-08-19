from Splits.Splits import Splits
from Splits.FileWriter import FileWriter
import sys

def main() -> int:

    args = sys.argv
    if(len(sys.argv) == 4):
        try:
            ab_threshold = int(args[1])
            hr_threshold = int(args[2])
            avg_threshold = float(args[3])
        except ValueError:
            print(f"\033[91m[ERROR] Arguments must be numbers: AB = {args[1]} HR = {args[2]} AVG = {args[3]}\033[0m")
            return -1
        
    elif(len(sys.argv) == 1):
        ab_threshold = 5 # 5, 1
        hr_threshold = 1 # 1, 1
        avg_threshold = .200 # .200, .300
    else:
        print(f"\033[91m[ERROR] Invalid number of arguments\033[0m")
        return -2
    
    try:
        with Splits() as bot:
            if not bot.go_to_url():
                bot.teardown = True
                return -3

            final_players = bot.get_final_players(ab_threshold, hr_threshold, avg_threshold)

            file_writer = FileWriter("output.txt")

            file_writer.write_results(final_players, ab_threshold, hr_threshold, avg_threshold)
            
            bot.teardown = True

        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return -4


if __name__ == '__main__':
    print("\nExit code ", main())