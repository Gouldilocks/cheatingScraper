from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path='/usr/bin/firefox')

driver.get('markfontenot.net')