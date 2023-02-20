from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
driver.find_element(By.XPATH,src="https://m.media-amazon.com/images/G/01/gno/sprites/nav-sprite-global-1x-reorg3._CB634609711_.png").click()
