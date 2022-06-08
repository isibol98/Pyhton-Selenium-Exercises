from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    
    def signIn (self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
        time.sleep(1)

    def getFollowings(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(2)

        items = self.browser.find_elements(By.CSS_SELECTOR, "#js-pjax-container > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div")

        for i in items:
            self.followers.append(i.find_element(By.XPATH, "//*[@id='js-pjax-container']/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a/span[1]").text)


github = Github(username, password)
github.signIn()
github.getFollowings()
print(github.followings)
        
