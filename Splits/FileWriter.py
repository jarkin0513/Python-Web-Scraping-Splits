from datetime import datetime

class FileWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def write_results(self, data: list, ab_threshold, hr_threshold, avg_threshold) -> None:
        try:
            teams = {}
            for team, player in data:
                if team not in teams:
                    teams[team] = []
                teams[team].append(player)

            with open(self.filename, 'w', encoding='utf-8') as file:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Generated on: {now}\n\n")

                file.write(self.add_thresholds(ab_threshold, hr_threshold, avg_threshold))
                file.write("----------------------------------\n\n")

                for team, players in sorted(teams.items()):

                    file.write(f"Team: {team}\n")

                    for player in players:

                        file.write(f"  - {player}\n")

                    file.write("-----------------------------------\n")
                    file.write("\n")

            print(f"\033[92m[INFO] Results successfully written to {self.filename}\033[0m")

        except Exception as e:
            print(f"\033[91m[ERROR] Failed to write to file: {e}\033[0m")

    def add_thresholds(self, ab, hr, avg):
        threshold_str = f"With thresholds against next OPP pitcher:\n    At least {ab} AB\n    Less than {hr} HR\n    At or below {avg} AVG\n\n"
        return threshold_str