from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver


def driver(url: str):
    #Start browser in HEADLESS MODE
    # options = FirefoxOptions()
    # options.add_argument("--headless")
    # browser = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
    # browser.get(url)

    #Start browser in VISUAL MODE
    browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    browser.get(url)

    return browser