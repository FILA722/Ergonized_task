from selenium.webdriver.common.by import By

class DiscordLocators():
    OPEN_DISCORD_BUTTON = (By.CSS_SELECTOR, 'button.button-ZGMevK:nth-child(2)')
    USERNAME_INPUT_FIELD = (By.CSS_SELECTOR, '.username-1XgXmI')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.button-ZGMevK:nth-child(2)')
    I_AM_HUMAN_FRAME = (By.CSS_SELECTOR,'#anchor-tc')
    I_AM_HUMAN_CHECKBOX = (By.CSS_SELECTOR, '#checkbox')
    WELCOME_FRAME = (By.CSS_SELECTOR, '.content--PpnxZ')
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, '.inputMonth-2nV8eY')
    DAY_OF_BIRTH = (By.CSS_SELECTOR, '.inputDay-2aeDxX')
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, '.inputYear-3RUSr9 > div:nth-child(1) > div:nth-child(1)')
  
