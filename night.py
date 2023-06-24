from time import sleep
from instabot import Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Replace <username> and <password> with your Instagram login credentials
username = "chintudon123@gmail.com"
password = "dickhead123"

# Replace <recipient_username> with the Instagram username of the person you want to text
recipient_username = "chaturya_vasudev"

# Replace <goodnight_message> with the message you want to send
goodnight_message = "Goodnight!"

# # Initialize the bot and log in to Instagram
# bot = Bot()
# bot.login(username=username, password=password)

# Open the Instagram direct messages page using Selenium
driver = webdriver.Chrome()
driver.get(
    "https://www.instagram.com/direct/t/340282366841710300949128153916569433696")
driver.implicitly_wait(10)
driver.maximize_window()
sleep(2)
driver.find_element(
    By.XPATH, "//button[contains(text(),'Allow essential and optional cookies')]").click()
sleep(4)

# Wait for the page to load and log in to Instagram using Selenium
driver.find_element(
    By.XPATH, "//span[contains(text(),'Log in with Facebook')]").click()
sleep(4)

driver.find_element(
    By.XPATH, "//button[contains(text(),'Only allow essential cookies')]").click()

driver.find_element(
    By.XPATH, "//input[contains(@id,'email')]").send_keys(username)
driver.find_element(
    By.XPATH, "//input[contains(@id,'pass')]").send_keys(password)
driver.find_element(By.XPATH, "//button[contains(@id,'loginbutton')]").click()

# Wait for the page to load and navigate to the conversation with the recipient using Selenium
sleep(5)
driver.find_element(
    By.XPATH, "//span[contains(text(),'chintuvedanth')]/../..//div[contains(text(),'Log In')]").click()
sleep(5)

driver.find_element(
    By.XPATH, "//button[contains(text(),'Not Now')]").click()
# Wait for the page to load and send the goodnight message using Selenium
sleep(5)

driver.find_element(
    By.XPATH, "//textarea[contains(@placeholder,'Message')]").send_keys(goodnight_message)
sleep(3)

driver.find_element(
    By.XPATH, "//div[contains(text(),'Send')]").click()
sleep(3)

# Close the browser window
driver.quit()


# Log out of Instagram using the bot
# bot.logout()
