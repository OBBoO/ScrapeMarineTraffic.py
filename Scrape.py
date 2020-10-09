import getpass
import pandas as pd
import requests
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

IMO_numbers = #List IMO

URL = "https://www.marinetraffic.com/en/ais/details/ships/imo:"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")

chrome_path = #'chromedriver PATH'

dic=[]

for link in IMO_numbers:
    
    driver = webdriver.Chrome(options=options, executable_path=chrome_path)
    
    classpath=driver.find_elements_by_xpath("//div[@class='MuiTypography-root MuiTypography-body1 MuiTypography-gutterBottom']")
    
    classpath2=driver.find_elements_by_xpath("//*[@class='MuiTypography-root MuiTypography-body1 MuiTypography-colorTextPrimary MuiTypography-gutterBottom']")
    
    driver.get(URL+str(link))
    
    for x in driver.find_elements_by_xpath("//h1[@class='MuiTypography-root MuiTypography-h4 MuiTypography-colorInherit']"):
        
        name=x.text
    
    position=driver.find_element_by_xpath("//a[@class='MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary MuiTypography-displayInline']").text
    
    latitude=position.split()[0].replace('°', '')
    
    longitude=position.split()[2].replace('°', '') 
    
    dic.append({
        'imo': imo,
        'name':name,
        'latitude': latitude,
        'longitude': longitude,
    })
    time.sleep(5)

dic = pd.DataFrame(dic)

print(dic)

dic.to_excel('res_scraping.xlsx')
