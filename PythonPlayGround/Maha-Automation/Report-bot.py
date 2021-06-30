from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import json


options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get("https://mahaicbs.mahamf.com:8443/")

time.sleep(20)
print('Page Loading finished!!')

userID = driver.find_element_by_xpath('//*[@id="divMainframe"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input')
userID.send_keys('yanpaingkyaw')

password = driver.find_element_by_xpath('//*[@id="divMainframe"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input')
password.send_keys('asd123!@#')

#select branch dropdox to ALL BRANCHES
branch = driver.find_element_by_xpath('//*[@id="divMainframe"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/select')
sel = Select(branch)
#sel.select_by_visible_text('ALL BRANCHES') //alternative way to select it
sel.select_by_value('999')
time.sleep(5)

#logIn
btnLogin = driver.find_element_by_xpath('//*[@id="divMainframe"]/table/tbody/tr[2]/td/fieldset/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/button')
btnLogin.click()
time.sleep(2)
print("Login Successfully!!!")

#click reportTab
reportTab = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/a')
reportTab.click()
time.sleep(2)

#click Loan Report
lnkReport = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/div')
lnkReport.click()
time.sleep(2)

#
# editing Report Parameters
#
reportType = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[2]/div/div/div/div/div[3]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/select')
rtSelect = Select(reportType)
rtSelect.select_by_value('LoanOutstanding')
time.sleep(2)

branchDD = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[2]/div/div/div/div/div[3]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/input')
branchDD.click()
time.sleep(5)

branchDropdown = driver.find_element_by_xpath('//*[@id="gwt-uid-553"]')
branchDropdown.click()
time.sleep(7)

branchDD = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[2]/div/div/div/div/div[3]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/input')
branchDD.click()
time.sleep(5)

#currency selection

currency = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[2]/div/div/div/div/div[3]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/select')
cSelect = Select(currency)
cSelect.select_by_value('MMK')
time.sleep(2)
currency.click()
time.sleep(2)

print("Input Parameter Successfully!!!")

#click ExportButton
btnExport = driver.find_element_by_xpath('//*[@id="divMainframe"]/div/div/table/tbody[2]/tr[2]/td[2]/div/div/div/div/div[3]/div/div[2]/div/div[2]/table/tbody/tr[8]/td[2]/button[2]')
btnExport.click()
time.sleep(5)
print("Generated Report!!")

