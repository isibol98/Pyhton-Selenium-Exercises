from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn (self):
    
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.NAME, "text")
        usernameInput.send_keys(self.username)
        time.sleep(2)
        nextButton = self.browser.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
        nextButton.click()
        time.sleep(2)
        passwordInput = self.browser.find_element(By.NAME, "password")
        passwordInput.send_keys(self.password)
        time.sleep(2)
        logInButton = self.browser.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
        logInButton.click()
        time.sleep(2)

    def search (self):
        self.browser.maximize_window()
        time.sleep(1)
        searchInput = self.browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys("python")
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)

twitter = Twitter(username, password)
twitter.signIn()
twitter.search()