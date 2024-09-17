from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape(url):

    #Setting up Chromdriver and passing it the url 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    #Attempting to scrape the webpage 
    #Waiting to quit the chromedriver until desired html is loaded on the page 
    try:
        WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.CLASS_NAME, 'label-e0291710e17e8c18f43f')))
    except:
        print("Odds didn't load in time")
    finally:
        data = driver.page_source  # Capture the HTML after JavaScript has rendered
        driver.quit()

    soup = BeautifulSoup(data, 'html.parser')
    return soup

def scrapeOdds(soup):
    #Scraping the handicap for each football game on Pinnacle that is not live 
    allOdds = soup.find_all('span', class_='label-e0291710e17e8c18f43f')
    odds = [item.text.strip() for item in allOdds]
    return odds

def scrapeTeams(soup):
    #Scraping the team names for all the games where we are scraping odds
    allTeams = soup.find_all('span', class_='ellipsis event-row-participant participant-e4bea5402c4da811c6b7')
    teams = [item.text.strip() for item in allTeams]
    return teams

def display_matchups(teams, odds):
    # Ensure teams and odds are grouped in pairs
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i + 1]
        odd1 = odds[i]
        odd2 = odds[i + 1]
        print(f"{team1} vs {team2}: {odd1}, {odd2}")

def main ():
    url = "https://www.pinnacle.com/en/football/matchups/"
    soup = scrape(url)
    games = soup.find_all('div', class_='row-d92d06fbd3b09cc856bc')
    for game in games:
        odds = scrapeOdds(game)
        teams = scrapeTeams(game)
        display_matchups(teams, odds)

if __name__ == "__main__":
    main()