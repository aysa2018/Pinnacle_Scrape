# Web Scraping Pinnacle Football Matchups

## Description and Purpose of the Project
This project scrapes the game spreads and corresponding team names for upcoming NFL and college football games from [Pinnacle.com](https://www.pinnacle.com/en/), which is renowned for providing some of the most accurate betting odds. By comparing Pinnacle's odds with those of other sportsbooks, customers can use the gathered data to discover positive Expected Value (EV) bets and steer clear of negative EV bets. The tool is especially helpful for sports bettors who want to base their choices on the best odds available in the market.

## Why did we choose Pinnacle?
Pinnacle is a well-known sportsbook that focuses on providing precise lines that frequently outperform those of competitors.  Bettors, or anyone who is interested to bet on the games can take advantage of this by:
- **Locating Positive EV Bets**: Examine your sportsbook's odds in comparison to Pinnacle's, and look for circumstances in which your sportsbook has more favorable odds than Pinnacle, indicating possible value.
- **Avoid Negative EV Bets**: To lower the chance of placing a losing long-term wager, stay away from wagers where your sportsbook has odds that are lower than Pinnacle.

## Features
- Scrapes football matchups from Pinnacle.
- Retrieves team names and their respective odds.
- Uses Selenium to handle dynamic page content that is rendered by JavaScript.
- Ensures the webpage is fully loaded before scraping by using explicit waits.

## Requirements
- Python 3.x
- Google Chrome browser installed
- ChromeDriver (automatically managed by webdriver_manager)

## Data Collected
The scraper retrieves the following data for each football game:
- **Team Names**: The two teams playing in each upcoming game.
- **Spread Odds**: The point spread odds for both teams.

## Installation

1. Clone the repository: (Type the following on your terminal)

```
git clone https://github.com/aysa2018/Pinnacle_Scrape
cd Pinnacle_Scrape

```

2. Install the required dependencies:(Type the following on your terminal)

```
pip install -r requirements.txt
```

or 

```
pip3 install -r requirements.txt
```

## How to Run

1. Execute the script: (Type the following on your terminal)
```
python main.py
```

or 

```
python3 main.py
```




