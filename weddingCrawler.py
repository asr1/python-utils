#! python3
# weddingCrawler.py - Downloads every wedding photo
#Two known bugs: 1. Grabs the last image twice. 2. Never grabs the first image. 

import requests, os, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import urllib.request

mycount = [24, 65, 71, 47, 68, 170, 308] #photos in each album

urls = [
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=7b4bbc63c31a2322bf82a5e1a5d54bab',
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=e5db3900436d71ef139e9051c8433582',
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=1f5a07a2d956b884c457cd92083f989a',
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=76e61320b47bca9a81e3cfc64cc8213f',
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=ea4c32e7fdc3dffdf470c12e866e11d7',
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=393c185b0935546690fb5a460c673511',
#'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=5a1079b8b319d730f089f34c4a45fbf9'
'https://www.fusionedgephotography.com/clients/index.php'
]

subUrls = [ #albums
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=7b4bbc63c31a2322bf82a5e1a5d54bab',
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=e5db3900436d71ef139e9051c8433582',
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=1f5a07a2d956b884c457cd92083f989a',
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=76e61320b47bca9a81e3cfc64cc8213f',
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=ea4c32e7fdc3dffdf470c12e866e11d7',
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=393c185b0935546690fb5a460c673511',
'https://www.fusionedgephotography.com/clients/online-viewing/alexcourtney-wedding-day/?sub=5a1079b8b319d730f089f34c4a45fbf9'
]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='d:/path/chromedriver.exe', options=options)

count = 1
dirCount = 1
for url in urls:
	os.makedirs('weddingPics', exist_ok=True)    # store comics in ./weddingPics
	print(url)
	driver.get(url)
	
	#login
	passElems = driver.find_elements_by_name('pagepass');
	if(passElems):
		passElems[0].send_keys('wedding')
		passElems[0].send_keys(Keys.ENTER)
	
	#find galleries
	#galleries = driver.find_elements_by_class_name('flexthumbnails')
	for link in subUrls:
		count = 1
		time.sleep(2)
		#gal.send_click()
		print(link)
		driver.get(link)
		time.sleep(2)
		thumbs = driver.find_elements_by_class_name('stackedthumbs')
		print('there are ' + str(len(thumbs)) + ' images')
		
	
		#save thumb
		#for thumb in thumbs:
		thumbs[0].click()
		time.sleep(2)

		
		# more_img = True
		# last_img = False
		
		#while(more_img):
		while(count <= mycount[dirCount-1]): # How many pictures are in this directory
			# if(last_img): #Python doesn't have a do-while loop, but there's certainly a cleaner way to do this.
				# more_img = False 
			time.sleep(2)
			img = driver.find_element_by_class_name('photoviewphoto')
			src = img.get_attribute('src')
			print(src)
			
			#Save file
			opener = urllib.request.build_opener()
			opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36')] #Lie to avoid 406
			urllib.request.install_opener(opener)
			urllib.request.urlretrieve(src, 'weddingPics/' + str(dirCount) + '/' + str(count) + ".png")
			print('downloading picture ' + str(count) + ' of ' + str(mycount[dirCount-1]))
			count = count + 1
			
			time.sleep(2)
			driver.execute_script("navigatephotos('next', 1)");
			
			
			#If the button exists, click it and continue
			# next_buttons = driver.find_elements_by_id('sy-photo-nav-next')
			# driver.implicitly_wait(10) # seconds
			# if(next_buttons):
				# next = driver.find_element_by_xpath('//*[@id="sy-photo-nav-next"]')
				# print(next)
				# next.click()
# #@				ActionChains(driver).move_to_element(next).click().perform()

			# else:
				# last_img = True
	
		# Next subURL
		dirCount = dirCount + 1
		time.sleep(2)
	

#driver.close()
print('Done.')