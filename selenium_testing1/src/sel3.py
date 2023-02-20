from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://www.amazon.com")
#driver.find_element_by_name('q').send_keys("selenium tutorial")
#driver.find_element("name","field-keywords").send_keys("Kurtas")
driver.find_element("name","field-keywords").send_keys("Selenium tutorials python")
Gmail=driver.find_element("Xpath","//*[@id='gb']/div/div[1]/div/div[1]/a").click()
driver.find_element(Gmail.LINK_TEXT, 'Login').click()


