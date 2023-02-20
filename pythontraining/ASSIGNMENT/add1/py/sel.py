from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")
# to maximize the browser window
#driver.maximize_window()
#get method to launch the URL
driver.get("https://www.amazon.com")
#to refresh the browser
driver.refresh()
#to close the browser


