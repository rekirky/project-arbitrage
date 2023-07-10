def sportsbet():
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
    #start_time = time.time()
    #changing chromedriver default options
    options = Options()
    # Run headless (disable if you want to view the browser / debug)
    options.add_argument('--headless')
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
    print(teams1)
    for team in teams1:
        team1.append(team.text)
    teams2 = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="participant-two"]')
    for team in teams2:
        team2.append(team.text)
    prices = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="price-text"]') 
    #for price in prices:
     #   oddsraw.append(price.text)
    #for i in range(0, len(oddsraw), 4):
     #   group = oddsraw[i:i+4]
      #  odds.extend(group[:2])
        
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

print(sportsbet())