from start_browser import driver
from web_locators import DiscordLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from validators import check_email, passwd_generator

username = input('Enter your username: ')
passwd = passwd_generator()

email = input('Enter your email: ')
email_is_valid = False
while not email_is_valid:
    if not check_email(email):
        email = input('Please enter your valid email: ')
    else:
        break

url = 'https://discord.com/'
try:
    browser = driver(url)
    wait = WebDriverWait(browser, 30)
    username = 'ryorgan12'

    open_discord_button = browser.find_element(*DiscordLocators.OPEN_DISCORD_BUTTON)
    open_discord_button.click()

    username_input_field = browser.find_element(*DiscordLocators.USERNAME_INPUT_FIELD)
    username_input_field.send_keys(username)

    login_button = browser.find_element(*DiscordLocators.LOGIN_BUTTON)
    login_button.click()

    welcome_frame = wait.until(EC.visibility_of_element_located(*DiscordLocators.WELCOME_FRAME))

finally:
    time.sleep(30)
    browser.quit()
