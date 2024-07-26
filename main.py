from Splits.Splits import Splits
import time

def main():
    inst = Splits()
    inst.go_to_url()
    inst.write_file()
    
    inst.get_players()

    time.sleep(30)

    inst.close()




if __name__ == '__main__':
    main()