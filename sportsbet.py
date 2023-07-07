#import libraries
#libraries subection 1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#libraries subsection 2
import pandas as pd
import pickle
import datetime
import re

start_time = time.time()
#changing chromedriver default options
options = Options()
# Run headless (disable if you want to view the browser / debug)
#options.add_argument('--headless')

team1 = []
team2 = []
oddsraw = []
odds = []
dict = {}

def sportsbet():
    team1 = []
    team2 = []
    oddsraw = []
    odds = []
    dict = {}
    web = 'https://www.sportsbet.com.au/betting/rugby-league/nrl'    
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    time.sleep(2)
   
   # Get teams and odds
    teams1 = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="participant-one"]')
    for team in teams1:
        team1.append(team.text)
    teams2 = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="participant-two"]')
    for team in teams2:
        team2.append(team.text)
    prices = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="price-text"]') 
    for price in prices:
        oddsraw.append(price.text)
    for i in range(0, len(oddsraw), 6):
        group = oddsraw[i:i+6]
        odds.extend(group[:2])
        
    # Make Dictionary of odds
    matches = []
    for i in range(len(teams1)):
        data_dict = {}
        data_dict['team1'] = team1[i]
        data_dict['team1odds'] = odds[i*2]
        data_dict['team2'] = team2[i]
        data_dict['team2odds'] = odds[i*2 +1]
        matches.append(data_dict)
    return(matches)

def bet365():
    # This may not work - they have anti-scraping procedures on their website
    # Investigate the bet365 api which may not be .com.au 
    team1 = []
    team2 = []
    oddsraw = []
    odds = []
    dict = {}
    web = 'https://www.bet365.com.au/#/AC/B19/C20459137/D50/E190002/F50/'    
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    time.sleep(20)
   
   # Get teams and odds
    teams1 = element = driver.find_element(By.CSS_SELECTOR, 'src-ParticipantFixtureDetailsHigher_Team')
    for team in teams1:
        team1.append(team.text)
    
    def tem(): 
        teams2 = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="participant-two"]')
        for team in teams2:
            team2.append(team.text)
        prices = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="price-text"]') 
        for price in prices:
            oddsraw.append(price.text)
        for i in range(0, len(oddsraw), 6):
            group = oddsraw[i:i+6]
            odds.extend(group[:2])
            
        # Make Dictionary of odds
        matches = []
        for i in range(len(teams1)):
            data_dict = {}
            data_dict['team1'] = team1[i]
            data_dict['team1odds'] = odds[i*2]
            data_dict['team2'] = team2[i]
            data_dict['team2odds'] = odds[i*2 +1]
            matches.append(data_dict)
        return(matches)


#sportsbetodds = sportsbet()
bet365odds = bet365()

print(sportsbetodds)