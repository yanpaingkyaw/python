from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import json


options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get("https://hana.finflux.io/")

time.sleep(30)

#userID_X = driver.find_element_by_xpath("//*[@id='uid']")
userID = driver.find_element_by_id('uid')
print("uesrID",userID)

userID.send_keys('yanpk')
password = driver.find_element_by_id('pwd')
password.send_keys('h@dmin123')

#logIn
btnLogin = driver.find_element_by_id('login-button')
btnLogin.click()
time.sleep(2)
#click reportTab
lnkReport = driver.find_element_by_xpath('//*[@id="main-menu-left"]/li[3]/a')
lnkReport.click()
time.sleep(2)
#GeneralTab
lnkGeneraltab = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/div/div/ul/li[4]/a')
lnkGeneraltab.click()
time.sleep(2)
#searchReport
txtsearchrpt = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/div/div/div/div[4]/div/input')
txtsearchrpt.send_keys('HANA - DailyClosure Status')
time.sleep(2)
#clicksearch result report
lnkQResult = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/div/div/div/div[4]/div/table/tbody/tr/td[1]') 
lnkQResult.click()
time.sleep(2)
#click run report
btnRunreport = driver.find_element_by_xpath('//*[@id="run"]')
btnRunreport.click()
time.sleep(2)
#GeneralTab
lnkGeneraltab = driver.find_element_by_xpath('//*[@id=""main]/div[2]/div/div/div/div/div/div/ul/li[4]/a')
lnkGeneraltab.click()
time.sleep(20)
#requstTab
lnkRequesttab = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/div/div/ul/li[1]/a')
lnkRequesttab.click()
time.sleep(2)
#click Download icon
lnkDownload = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[2]')
lnkDownload.click()
time.sleep(2)




