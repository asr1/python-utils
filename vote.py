from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

count = 0
while(True):
	driver = webdriver.Chrome(executable_path='d:/path/chromedriver.exe')
	driver.get("https://www.i77express.com/about-us/in-the-community/purposeful-giving-contest/")
	# assert "Python" in driver.title
	driver.implicitly_wait(10) # seconds
	elem = driver.find_element_by_xpath('//*[@id="totalpoll-id-76a970e19557b7ec2226b0a737139b07"]/form/div[1]/label[1]/div') #select candidate
	elem.click()
	button = driver.find_element_by_name("totalpoll[action]") # vote button
	button = driver.find_element_by_xpath('//*[@id="totalpoll-id-76a970e19557b7ec2226b0a737139b07"]/form/div[2]/button[2]') # vote button
	button.click()
	count = count + 1
	print(count)
	time.sleep(100)
	driver.close()
