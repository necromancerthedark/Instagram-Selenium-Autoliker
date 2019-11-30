##Instagram Autoliker Bot By Kumar Gaurav Pandey aka Necromancerthedark:
#what it does?
#Likes all Photos of profile you provide

#import all the module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import getpass
import re
from selenium.webdriver.common.action_chains import ActionChains

#Inputting initials
input_username =input("Enter Your Insta Username: ")
input_password =getpass.getpass("Enter Your Password:" )
Search_profile =input("Enter the Exact Username of Person You want to search: ")
scroll_counter =1
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(5)

username= driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")
username.send_keys(input_username)
password.send_keys(input_password)
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

time.sleep(10)
try:
    not_now = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    not_now.click()
except:
    print("Sorry an Error Encountered!!")

try:
    searchbar = driver.find_element_by_xpath("//input[@placeholder='Search']")
    searchbar.send_keys(Search_profile)
    time.sleep(10)
    searchbar.send_keys(Keys.ARROW_DOWN)
    searchbar.send_keys(Keys.ENTER)
except:
    print("not found")

time.sleep(10)
first_photo = driver.find_element_by_class_name('_9AhH0')
first_photo.click()

time.sleep(10)

while(scroll_counter==1):
    try:
        image_link = driver.find_element_by_xpath("//div[@role='button']")
        doubleclickable = ActionChains(driver)
        doubleclickable.double_click(image_link)
        doubleclickable.perform()
        next_button = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
        next_button.click()

        time.sleep(5)
    except:
        scroll_counter=2
        print("Thank You For Using My Bot!")

try:
    os.system('pause')
except:
    os.system('read -n1 -r -p "Press any key to continue..." key')
