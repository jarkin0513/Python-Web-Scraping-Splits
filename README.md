# Python-Web-Scraping-Splits

The purpose of this project is to use the Selenium library to create a script that will automatically scrape information about baseball games from a website. Using this information and a formula, it will write to a text file that will show players who should be bet on to hit under 0.5 homeruns in their next game. 
The formula is simple and pretty much relies on: 
1) Only pick players from the underdog team
2) Only pick players who have or are below .200 AVG against the pitcher they will face
3)  Only players who have at least 5 AB against that pitcher
4)  Only players who have no home runs hit against that pitcher

This may change and be adjusted, but it is a good spot to go off of for the time being.
The odds for these picks are always pretty bad so it is not exactly the best strategy. I do not really intend on actually using this with real money. I thought it was just good inspiration for a project to learn about Selenium and web scraping in general.

---

## Installation and Running the App

Pre-built executables are available for Windows and macOS. **No need to install Python or any dependencies** — just download the correct file for your platform.

> **Note**: **Google Chrome must be installed** on your system. The app uses the bundled `chromedriver` version `137.0.7151.68`, which is compatible with Chrome version 137. If you have a different version of Chrome installed, you may encounter compatibility issues.

### Windows Users

1. Download the latest `.exe` file from the [Releases](https://github.com/jarkin0513/Python-Web-Scraping-Splits/releases) page: <br>
    `SplitsScraper-Windows`

2. **Important**: When running for the first time, Windows Defender SmartScreen may warn you because the file is unsigned. 
- Click **"More Info"** → **"Run Anyway"** to proceed.

3. Double-click the `.exe` file to run it.

4. The program will:
- Open Chrome automatically.
- Scrape the relevant data.
- Write results to an `output.txt` file located in the same folder as the `.exe`.

---

### macOS Users

There are separate downloads for different Mac processors:

| Chip Type       | Download File                |
|-----------------|-------------------------------|
| Intel-based Macs | `SplitsScraper-Mac-Intel`    |
| Apple Silicon (M1, M2, M3) | `SplitsScraper-Mac-ARM64` |

1. Download the correct file from the [Releases](https://github.com/jarkin0513/Python-Web-Scraping-Splits/releases) page based on your Mac's chip.
2. After downloading:
- Open **Terminal**.
- Navigate to the folder containing the downloaded file:
  ```bash
  cd /path/to/your/downloads
  ```
- Make the app executable:
  ```bash
  chmod +x SplitsScraper-Mac-Intel
  ```
  or
  ```bash
  chmod +x SplitsScraper-Mac-ARM64
  ```

3. Run the program:<br>
```./SplitsScraper-Mac-Intel```<br>
or<br>
```./SplitsScraper-Mac-ARM64```

> **Note for Mac users:**: This app is currently provided as a standalone executable file, not a ```.app``` bundle.
macOS requires Terminal to run raw executables downloaded from the Internet.
Double-click launching is not available at this time.
(I may add a double-clickable ```.app``` version in the future!)

5. The program will:
  - Open Chrome automatically.
  - Scrape the relevant data.
  - Write results to an output.txt file located in the same folder as the executable.

## Frequently Asked Questions

### Why does Windows block the .exe?
Windows Defender SmartScreen flags all unsigned executables by default. This project is not digitally signed yet. You can safely run the app by clicking More Info → Run Anyway.

### Do I need Python installed?
No. The provided .exe and Mac executables are standalone — no Python environment or libraries are needed.

### Where does the output go?
The program writes the list of selected players to a file called:
```output.txt```.
This file will be created in the same folder as the executable.

### Does Chrome need to be installed?
Yes. Chrome is required because the app uses Selenium to automate web scraping through Chrome. The bundled ```chromedriver``` is version ```137.0.7151.68```, compatible with Chrome version 137. If your version of Chrome is very different, you may need to update Chrome or use a matching chromedriver.

You can download the latest Google Chrome [here](https://www.google.com/chrome/).

## Development Setup (For Contributors)
If you wish to work with the source code directly:

1. Clone the repository:
   ```
       git clone https://github.com/jarkin0513/Python-Web-Scraping-Splits.git
       cd yourrepo
   ```
2. Install the required Python packages:
   ```pip install -r requirements.txt```
3. Download the appropriate version of ```chromedriver``` that matches your installed version of Google Chrome:

    - You can check your Chrome version by navigating to:
      ```chrome://version/```

    - Download the matching chromedriver [here](https://developer.chrome.com/docs/chromedriver/downloads).
  
4.  Place the downloaded ```chromedriver``` binary inside the ```Splits/``` directory:
    ```
    yourrepo/
    ├── main.py
    ├── Splits/
        ├── chromedriver    <-- place it here (no extension on Mac/Linux, .exe on Windows)
    ```

5. Run the script:
   ```python main.py```

---
Example snippet from [fantasyalarm.com](https://www.fantasyalarm.com/mlb/lineups).
![image](https://github.com/user-attachments/assets/a0633ce2-b60f-4240-8c81-4256e3544a79)
![image](https://github.com/user-attachments/assets/053756ac-34f8-417d-8508-bf2801357ea9)
![image](https://github.com/user-attachments/assets/04626da3-3d7b-4829-b4c1-90787e10c580)


## License
This project is for educational purposes only and is provided "as is" without warranty of any kind.
