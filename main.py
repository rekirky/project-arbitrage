# Modules
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

# Custom Functions
from sportsbet import sportsbet


print("run")
sportsbetodds = sportsbet()
print("run2")
print(sportsbetodds)
#bet365odds = bet365()

