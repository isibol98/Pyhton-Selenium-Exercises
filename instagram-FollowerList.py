from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
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
        time.sleep(3)

    def getFollowers (self):
        self.browser.get(f"https://www.instagram.com/{username}/followers/")
        time.sleep(3)

        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog] ul").find_elements(By.CSS_SELECTOR, "li")
        followerCount = len(followerList = dialog.find_elements(By.CSS_SELECTOR, "li"))
        print(f"First Follower Count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(followerList = dialog.find_elements(By.CSS_SELECTOR, "li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"Follower Count: {followerCount}")
                pass
            else:
                break

        followerList = dialog.find_elements(By.CSS_SELECTOR, "li")
        for user in followerList:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            print(link)



instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollowers()