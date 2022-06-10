from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstagramFollow:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver.exe", chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        
    def signIn (self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        
        usernameInput.send_keys(self.username)
        time.sleep(1)
        passwordInput.send_keys(self.password)
        time.sleep(1)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
        self.browser.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        time.sleep(3)
    def followUser (self, username):
        self.browser.get(f"https://instagram.com/{username}")
        time.sleep(2)

        try:
            followButton = self.browser.find_element(By.XPATH, "//div[text()='Follow']")
            followButton.click()
        except:
            print("Already following.")



instagramFollow = InstagramFollow(username, password)
instagramFollow.signIn()
instagramFollow.followUser(input("Enter username: "))