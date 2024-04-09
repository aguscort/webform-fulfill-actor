from selenium import webdriver
import os
import argparse

class fulfillForm():
    # Parameters
    __visible =False

    # Credentials
    def __init__ (self, firstname, surname, phone, email, code, url, visible):
        self.__visible =visible
        self.__firstname = firstname
        self.__surname = surname
        self.__phone = phone
        self.__email = email
        self.__code = code
        self.__url = url

    def proceed(self):
        self.__results =[]

        driver_location ='c:\\chromedriver\\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] =driver_location
        if self.__visible:
            driver =webdriver.Chrome(driver_location)
        else:
            chrome_options =Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("download.default_directory=" + download_path)
            driver =webdriver.Chrome(driver_location, chrome_options=chrome_options)

        print ("Checking ...")
        driver.implicitly_wait(10)
        driver.get(self.__url)

        # # Perform the login
        driver.find_element_by_xpath('//*[@id="firstname"]').send_keys(self.__firstname)
        driver.find_element_by_xpath('//*[@id="lastname"]').send_keys(self.__surname)
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.__phone)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.__email)
        driver.find_element_by_xpath('//*[@name="certificate"]').send_keys(self.__code)
        driver.find_element_by_xpath('//*[@name="updateqty"]').click()
        driver.find_element_by_xpath('//*[@id="agree-to-terms-checkbox"]').click()
        driver.find_element_by_xpath('//*[@name="paylater"]').click()

        time.sleep(30)
        driver.quit()


CLI=argparse.ArgumentParser()
CLI.add_argument("--firstname", help="firstname", type=str)
CLI.add_argument("--surname", help="surname", type=str)     
CLI.add_argument("--phone", help="phone", type=str) 
CLI.add_argument("--email", help="email", type=str) 
CLI.add_argument("--code", help="code", type=str) 
CLI.add_argument("--url", help="url", type=str) 
args = CLI.parse_args()

ff =fulfillForm(args.firstname, args.surname, args.phone, args.email, args.code, args.url, True)
ff.proceed(), 