from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com")
time.sleep(10)

username = "testest"
password = "********"

followingResult = []
followersResult = []


def scrollbarDown():
    # js code for scrollbar
    js = """
                page = document.querySelector(".isgrP");
                page.scrollTo(0,page.scrollHeight);
                var endofpage = page.scrollHeight;
                return endofpage;
            """
    endofpage = driver.execute_script(js)
    while True:
        end = endofpage
        time.sleep(1)
        endofpage = driver.execute_script(js)
        if end == endofpage:
            break


def login():
    usernameelement = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "username"))

    )
    usernameelement.send_keys(username)
    passwordelement = driver.find_element_by_name("password")
    passwordelement.send_keys(password)

    button = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
    button.click()

    notificationbutton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))
    )
    notificationbutton.click()


def goToProfile():
    profile1 = driver.find_element_by_xpath(
        "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
    profile1.click()
    time.sleep(2)

    profile2 = driver.find_element_by_xpath(
        "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div")
    profile2.click()
    time.sleep(2)


def getFollowings():
    following = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
    following.click()

    time.sleep(1)

    scrollbarDown()

    followingList = driver.find_elements_by_class_name("FPmhX")
    for i in followingList:
        followingResult.append(i.text)


def getFollowers():
    followers = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
    followers.click()

    time.sleep(1)

    scrollbarDown()

    followersList = driver.find_elements_by_class_name("FPmhX")
    for i in followersList:
        followersResult.append(i.text)


try:
    login()

    goToProfile()

    getFollowings()

    driver.back()
    time.sleep(5)
    getFollowers()

    doesntfollowyou = []
    for item in followingResult:
        if item not in followersResult:
            doesntfollowyou.append(item)
            print(item)
finally:
    driver.quit()
