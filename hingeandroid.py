from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

import time
import random
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Replace with your emulator device name
    "appPackage": "co.hinge.app",  # Replace with your app package name
    "appActivity": "co.hinge.app.ui.AppActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the app to open for 10 seconds
driver.implicitly_wait(10)

sign_in = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[2]"))
)
sign_in.click()

facebook = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[2]"))
)
facebook.click()

facebook_continue = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]"))
)
facebook_continue.click()


privacy = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (MobileBy.ID, "co.hinge.app:id/accept_all_button"))
)
privacy.click()

time.sleep(5)
driver.tap([(284, 1016)])
time.sleep(5)
driver.tap([(284, 1016)])

x_swipe = 550
y_start = 1800
like_num = 500
MAX_RETRIES = 3
WAIT_TIME = 2
for i in range(like_num):
    print(i)
    for k in range(MAX_RETRIES):
        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (MobileBy.ID, "co.hinge.app:id/like_button"))).click()
            break  # exit the loop if the click was successful
        except (TimeoutException, StaleElementReferenceException, NoSuchElementException):
            print(str(k+1) + " Swipe try")
            for j in range(4):
                print(str(j+1) + " Swipe action")
                action = TouchAction(driver)
                y_end = random.randint(300, 1000)
                action.press(x=x_swipe, y=y_start).move_to(
                    x=x_swipe, y=y_end).release().perform()
            time.sleep(WAIT_TIME)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (MobileBy.ID, "co.hinge.app:id/send_like_button"))).click()


print("Successfully liked " + str(like_num) + " people")
