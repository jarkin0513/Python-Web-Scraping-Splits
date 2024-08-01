from Splits.Splits import Splits
import time

def main():
    with Splits() as bot:
        bot.go_to_url()
        bot.write_file()
        bot.get_players()


        time.sleep(30)

        bot.close()




if __name__ == '__main__':
    main()