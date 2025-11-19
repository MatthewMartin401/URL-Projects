#  Project: Project-HmblBndl_BookSearch.
#  Creator: Me.
#  Status: Complete.

'''
This project is suppost to collect a list of all of the Books on offer in an Bundle on Humble Bundle,
and open a tab for each item. This is to be used for convience when looking into the contents of a bundle.
'''

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse
import sys


#  Goes to website and gets all items
URL = ""
if URL == "" or URL == None:
    # URL = input("Bundle URL: ")
    URL = str(sys.argv[1])  #  When used in Batch Scripts, index 0 is the script.
# print(len(sys.argv))
print(f"URL entered is: {URL}")
browser = webdriver.Chrome()
browser.get(URL)
itemName = "item-title"  #  Not loading in the html. Needs a delay which requests library doesn't support. Changed to Selenium.
itemNameList = []
browser.fullscreen_window()  #  Elements change depending on window size.
time.sleep(2)
text = browser.find_elements(By.CLASS_NAME, itemName)  #  Gets all of the items displayed on the page.

#  Converts to string and add items to list.
for webElem in list(text):
    itemNameList.append(str(webElem.text))
browser.quit()

#  Opens items within the browser.
searchURL = "https://www.google.com/search"  #  Search Engine url link.
for val in itemNameList:
    param = {'q' : str(val)}
    added_param = urllib.parse.urlencode(param)  #  Adds parameters onto URL
    encoded_url = f'{searchURL}?{added_param}'  #  Final URL
    webbrowser.open(url=encoded_url)