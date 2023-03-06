from selenium import webdriver 
from selenium.webdriver.common.by import By 
import chromedriver_autoinstaller 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 
 
# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
 
# Setting the driver path and requesting a page 
driver = webdriver.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

# Initializing a list with two Useragents 
useragentarray = [ 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", 
] 
for i in range(len(useragentarray)): 
	# Setting user agent iteratively as Chrome 108 and 107 
	driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
	print(driver.execute_script("return navigator.userAgent;")) 
	driver.get("https://www.grosvenorcasinos.com/slots-and-games/all") 
 
# Wait 10 on the webpage before trying anything 
time.sleep(1000) 
 
# Wait for 3 seconds until finding the html page source 
wait = WebDriverWait(driver, 3) 
html = driver.page_source

# Save the html source as a file
with open('saved.html', 'w') as f:
    f.write(html)
    f.close()
 
# Close the driver after 3 seconds 
time.sleep(3) 
driver.close()