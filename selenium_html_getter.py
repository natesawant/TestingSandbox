from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.grosvenorcasinos.com/slots-and-games/all')
browser.implicitly_wait(10)
html = browser.page_source

with open('saved.html', 'w') as f:
    f.write(html)
    f.close()

browser.close()