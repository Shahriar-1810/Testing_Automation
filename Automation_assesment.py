from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

#automatically install the current webdriver version
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(3)

#Navigate to url http://automationexercise.com
driver.get("http://automationexercise.com")
driver.maximize_window()

#Verify that home page is visible successfully
expected_title = "Automation Exercise"
expected_url = "https://automationexercise.com/"
if (driver.title==expected_title):
    print("Verified Home Page title 'Automation Exercise'")
else:
    print("Incorrect site")

if (driver.current_url==expected_url):
    print("Verified Home Page url")
else:
    print("Incorrect site")

time.sleep(3)
#Add products to cart

#driver.find_element(By.CSS_SELECTOR, 'a[data-product-id="1"]').click()
driver.find_element(By.LINK_TEXT, 'Add to cart').click()
time.sleep(3)


driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button').click()
time.sleep(3)

#Click Cart button
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a').click()
time.sleep(3)

#Verify that cart page is displayed
expected_title = "Automation Exercise - Checkout"
expected_url = "https://automationexercise.com/view_cart"
if (driver.title==expected_title):
    print("Verified Cart Page title 'Automation Exercise - Checkout'")
else:
    print("Incorrect site")

if (driver.current_url==expected_url):
    print("Verified Cart Page url")
else:
    print("Incorrect site")

#Click Proceed To Checkout
driver.find_element(By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a').click()
time.sleep(3)

#Click Register / Login button
driver.find_element(By.XPATH, '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a/u').click()
time.sleep(3)

#Filling name field in sigup form
driver.find_element(By.NAME, 'name').send_keys("Nafis")
time.sleep(2)

#Filling email field in sigup form
driver.find_element(By.CSS_SELECTOR,'input[data-qa="signup-email"]').send_keys("Nafis181000@gmail.com")
time.sleep(2)

#Clicking sign up button
driver.find_element(By.CSS_SELECTOR,'button[data-qa="signup-button"]').click()
time.sleep(3)

#Filling up the whole form for registration
#gender
driver.find_element(By.ID,'id_gender1').click()
time.sleep(2)

#password
driver.find_element(By.ID,'password').send_keys("nafis019")
time.sleep(2)

#day
days_select = Select(driver.find_element(By.ID,"days"))
days_select.select_by_value("18")
time.sleep(1)

#month
months_select = Select(driver.find_element(By.ID,"months"))
months_select.select_by_value("10")
time.sleep(1)

#year
years_select = Select(driver.find_element(By.ID,"years"))
years_select.select_by_value("1998")
time.sleep(1)

#newletter
driver.find_element(By.NAME,'newsletter').click()
time.sleep(2)


driver.find_element(By.ID,'first_name').send_keys("Nafis")
time.sleep(2)

driver.find_element(By.ID,'last_name').send_keys("Iqbal")
time.sleep(2)

driver.find_element(By.ID,'company').send_keys("Kinetik")
time.sleep(2)

driver.find_element(By.ID,'address1').send_keys("USA")
time.sleep(2)


country_select = Select(driver.find_element(By.ID,"country"))
country_select.select_by_value("United States")


driver.find_element(By.ID,'state').send_keys("USA")
time.sleep(2)

driver.find_element(By.ID,'city').send_keys("New York")
time.sleep(2)

driver.find_element(By.ID,'zipcode').send_keys("1216")
time.sleep(2)

driver.find_element(By.ID,'mobile_number').send_keys("0194830137621")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,'button[data-qa="create-account"]').click()
time.sleep(2)

#Verify that account is created
expected_title = "Automation Exercise - Account Created"
expected_url = "https://automationexercise.com/account_created"
if (driver.title==expected_title):
    print("Verified Account Created Page title 'Automation Exercise - Account Created'")
else:
    print("Incorrect site")

if (driver.current_url==expected_url):
    print("Verified Account Created url")
else:
    print("Incorrect site")

#click continue
driver.find_element(By.CSS_SELECTOR,'a[data-qa="continue-button"]').click()

#verify Logged in as username
expected_username = "Nafis"
logged_username= driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b').text
if (logged_username==expected_username):
    print("Logged in as correct username")
else:
    print("Logged in as incorrect username")

driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a').click()
time.sleep(2)

#Click Proceed To Checkout
driver.find_element(By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a').click()
time.sleep(2)

#Address details review
expected_name= "Mr. Nafis Iqbal"
expected_address1= "USA"
expected_address2= "New York USA 1216"
expected_city="United States"
expected_number= "0194830137621"

printed_name =driver.find_element(By.XPATH,'//*[@id="address_delivery"]/li[2]').text
printed_address1 =driver.find_element(By.XPATH,'//*[@id="address_delivery"]/li[4]').text
printed_address2 =driver.find_element(By.XPATH,'//*[@id="address_delivery"]/li[6]').text
printed_city =driver.find_element(By.XPATH,'//*[@id="address_delivery"]/li[7]').text
printed_number = driver.find_element(By.XPATH,'//*[@id="address_delivery"]/li[8]').text

if (expected_name==printed_name and expected_address1==printed_address1 and expected_address2==printed_address2 and expected_city==printed_city and expected_number==printed_number):
    print("Address details reviewd")
else:
    print("Wrong address details")


#order review
Product_name = "Blue Top"
printed_product_name = driver.find_element(By.XPATH,'//*[@id="product-1"]/td[2]/h4/a').text

if (Product_name==printed_product_name):
    print("Correct product")
else:
    print("wrong product")

time.sleep(3)
#Comment in text area
driver.find_element(By.XPATH,'//*[@id="ordermsg"]/textarea').send_keys("Great Website to practice automation")
time.sleep(2)

#click place order
driver.find_element(By.XPATH,'//*[@id="cart_items"]/div/div[7]/a').click()
time.sleep(2)

#entering payment details

#name on card
driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[1]/div/input').send_keys("Nafis Iqbal")
time.sleep(1)

#card no
driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[2]/div/input').send_keys("1111222233334444")
time.sleep(1)

#cvc
driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[3]/div[1]/input').send_keys("181")
time.sleep(1)

#MM
driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[3]/div[2]/input').send_keys("12")
time.sleep(1)

#YYYY
driver.find_element(By.XPATH,'//*[@id="payment-form"]/div[3]/div[3]/input').send_keys("2024")
time.sleep(2)

#click on Pay and confirm order
driver.find_element(By.XPATH,'//*[@id="submit"]').click()

#verify the success message
# Verify_message = "Your order has been placed successfully!"
# displayed_message = driver.find_element(By.XPATH,'//*[@id="success_message"]/div').text
#
# if (Verify_message==displayed_message):
#     print("Successful message verified")
# else:
#     print("wrong successful message")
