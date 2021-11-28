from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from Credents.credents import *

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get("https://www.instagram.com/")
sleep(2)


def login():
    username = driver.find_element(By.NAME, "username")
    username.click()
    username.send_keys(username1)
    pasw = driver.find_element(By.NAME, "password")
    pasw.click()
    pasw.send_keys(password1)
    button = driver.find_element(By.XPATH, '//button[@type="submit"] ')
    button.click()
    sleep(4)
    driver.find_element(By.XPATH, '//button[contains(text(),"Not Now")]').click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Not Now")]').click()


def mass_like():
    i = 1
    while i < 7:
        likebutton = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/section/main/section/div/div[2]/div/article[{}]/div/div[3]/div/div/section[1]/span[1]/button".format(
                                             i))
        likebutton.click()
        sleep(3)
        i += 1
        if i == 6:
            i = 4


def like_fpost():
    driver.find_element(By.XPATH, "//button[@class='wpO6b  ']").click()
    driver.find_element(By.XPATH, '//button[contains(text(),"Go to post")]').click()
    sleep(2)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()


def cmnt_post():
    driver.find_element(By.CLASS_NAME, "Ypffh").click()
    driver.find_element(By.CLASS_NAME, "Ypffh").send_keys("(◓̀ ₒ ́◓)")
    driver.find_element(By.XPATH, '//button[contains(text(),"Post")]').click()
    sleep(3)
    driver.back()
    sleep(2)


def check_msg():
    messages = driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
    messages.click()
    sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".qyrsm >font-weight=600").click()
    msg = driver.find_element(By.XPATH,
                              "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    msg.click()
    sleep(2)
    msg.send_keys("Bot Generated message:")
    driver.find_element(By.XPATH, '//button[contains(text(),"Send")]').click()
    sleep(2)
    msg.send_keys("Hello there, kindly message on the other account please.")
    driver.find_element(By.XPATH, '//button[contains(text(),"Send")]').click()
    sleep(2)
    driver.back()
    driver.back()


def follow():
    driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a').click()
    i = 1
    while True:
        try:
            sleep(1)
            get_button = driver.find_element(By.XPATH,
                                             '/html/body/div[1]/section/main/div/div[2]/div/div/div[{}]/div[3]/button'.format(
                                                 i))
            get_button.click()
            i += 1
        except NoSuchElementException:
            sleep(300)
            driver.refresh()
            sleep(2)


def stories():
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button').click()
    while True:
        driver.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div').click()


def like_all_posts():
    sleep(2)
    i = 0
    search = driver.find_element(By.XPATH, ''' //input*[@aria-label='Search Input'] ''')
    search.click()
    search.click()
    sleep(2)
    search.send_keys('_.Dharvi._')
    sleep(2)
    while (i < 1):
        id = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[{}]/a/div'.format(
                                     i))
        id.click()
        i = +1

# login()
# mass_like()
# like_fpost()
# cmnt_post()
# stories()
# check_msg()      *Few bugs
# follow()
# like_all_posts() *Few bufs
# like_all_posts() *Not Working
# driver.close()
