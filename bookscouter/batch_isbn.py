from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time 


browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
#browser.get('https://bookscouter.com//') 

#assert "Sell textbooks" in browser.title

file = open(sys.argv[1],"r")
barcodes = file.readlines()
file.close() 

tab = 0
win_num = 0
b = barcodes[0]

url = "https://bookscouter.com/sell/" + str(b) + "" 
browser.get(url) 


'''for i in range(len(barcodes)):
	b = barcodes[i]
	time.sleep(1)
	search = browser.find_element_by_class_name("input--text.input--search") #Find the search box by class
	search.send_keys(b) #send the value of search field
	time.sleep(1)
	submit_button = browser.find_element_by_class_name("btn.btn--accent.search__btn")
	submit_button.click()
	if i != (len(barcodes) - 1):
		script = "window.open('https://bookscouter.com/tools'," + str(win_num) + ")"
		browser.execute_script(script)
		tab += 1
		win_num += 1
		browser.switch_to.window(browser.window_handles[tab])
		browser.get('https://bookscouter.com/tools') 
		#time.sleep(5)
'''

for i in range(1, len(barcodes)):
	b = barcodes[i]
	time.sleep(1)
	
	if i != (len(barcodes) - 1):
		script = "window.open('https://bookscouter.com/tools'," + str(win_num) + ")"
		browser.execute_script(script)
		tab += 1
		win_num += 1
		browser.switch_to.window(browser.window_handles[tab])
		url = "https://bookscouter.com/sell/" + str(b) + "" 
		browser.get(url) 










