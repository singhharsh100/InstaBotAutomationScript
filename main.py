import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
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
            driver.back()
            sleep(2)
            break


def stories():
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button').click()
    while True:
        driver.find_element(By.XPATH, '/html/body/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div').click()


def like_all_posts():
    sleep(2)
    i = 1
    search = driver.find_element(By.XPATH, '''/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div''')
    search.click()
    search1 = driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    search1.click()
    sleep(2)
    search1.send_keys('manyatiwari25')
    sleep(2)

    id = driver.find_element(By.XPATH,
                             '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a'.format(
                                 i))
    id.click()
    sleep(2)
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]").click()
    i = + 1
    sleep(3)
    while (True):
        driver.find_element(By.XPATH,
                            '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]').click()
        driver.find_element(By.XPATH,
                            "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").click()
        driver.find_element(By.XPATH,
                            "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").send_keys(
            "(◓̀ ₒ ́◓)")
        sleep(2)
        driver.find_element(By.XPATH, '//button[contains(text(),"Post")]').click()
        sleep(4)
        driver.find_element(By.XPATH,
                            "//button[@class='wpO6b  ']//*[local-name() = 'svg'][@aria-label='Next']").click()
        sleep(3)


def mass_spam():
    i = 94
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a").click()
    sleep(2)
    while (True):
        q = 10
        sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/ul/div/li[2]").click()
        while (i > q):
            try:
                ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                sleep(3)
                driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]").click()
                ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                q = q + 6
                sleep(6)
                driver.find_element(By.XPATH,
                                    "/html/body/div[6]/div/div/div[3]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a".format(
                                        i)).click()
                sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
                sleep(3)
                msg = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                msg.click()
                sleep(2)
                msg.send_keys("ヾ(＾-＾)ノ")
                driver.find_element(By.XPATH, '//button[contains(text(),"Send")]').click()
                sleep(2)
                msg.send_keys("May all your troubles last as long as your New Year’s resolutions.")
                driver.find_element(By.XPATH, '//button[contains(text(),"Send")]').click()
                sleep(2)
                msg.send_keys("Happy New Year!!")
                driver.find_element(By.XPATH, '//button[contains(text(),"Send")]').click()
                sleep(2)
                driver.back()
                driver.back()
                sleep(3)
                driver.refresh()
                sleep(3)
                i += 1
            except selenium.common.exceptions.NoSuchElementException as exc:
                driver.refresh()


login()
# mass_like()      *Few bugs
#like_fpost()
#cmnt_post()
# stories()
# check_msg()  # *Few bugs
# follow()
#like_all_posts()
# driver.close()
# mass_spam()
