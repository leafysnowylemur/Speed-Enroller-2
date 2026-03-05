import datetime
import logging as log
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import main
import settings as s

def DevMode(driver):
    print("DEV MODE")
    for i in range(s.DEV_TABS):
        if i != 0:
            driver.switch_to.new_window('tab')
        driver.get("https://erau.collegescheduler.com/terms/Daytona-Prescott%202026%20Fall/cart")

        if login(driver) < 0:
            return -1

        try:
            element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Shopping Cart']")))
        except:
            print("Duo authentication timed out or failed")
            log.error("Duo authentication timed out or failed")
            driver.quit()
            return -1
        element.click()
        print("Clicked 'Shopping Cart'")

        if i == 0:
            driver.get("https://erau.collegescheduler.com/terms/Daytona-Prescott%202026%20Fall/cart")
        
        try:
            element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']")))
        except:
            log.error("Register Click Failed")
            print("Register Click Failed")
            driver.quit()
            return -1
        element.click()
        print("Clicked 'Register'")

    delta = 5 / (s.DEV_TABS - 3)
    split = 3

    for i in range(s.DEV_TABS):
        driver.switch_to.window(driver.window_handles[i])
        timeleft = 0
        while (datetime.datetime.now() < s.targetTime - datetime.timedelta(seconds=split)):
            #print("sleeping in the loop thing")
            sleep(.0001)
            newTimeleft = datetime.timedelta(seconds = (s.targetTime - datetime.datetime.now()).seconds)
            if newTimeleft != timeleft:
                timeleft = newTimeleft
                print(f"Time left: {timeleft.seconds} seconds")
        split -= delta

        driver.find_element(By.XPATH, f"//button[text()='{s.CLICKTEXT}']").click()
        #driver.find_element_by_xpath(f"//button[text()='{s.CLICKTEXT}']").click()
    
    #print("sleeping for 60 seconds")
    #sleep(60)

    return 0

def login(driver):
    try:
        element = WebDriverWait(driver, s.SHOPPING_CART_DELAY).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log In']")))
    except:
        if (not driver.find_element_by_xpath("//span[text()='Shopping Cart']")):
            log.error("Log in button not found")
            print("Login button not found")
            driver.quit()
            return -1
        else:
            return 0
    driver.find_element_by_id("username").send_keys(s.id)
    driver.find_element_by_id("inputPassword").send_keys(s.pw)
    element.click()
    return 0

if __name__ == '__main__':
    main.main()