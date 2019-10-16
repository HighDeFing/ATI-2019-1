from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5000/home.html")

#navegacion user
#desde trivias a todos 
element=driver.find_element_by_xpath("//*[contains(text(), 'User Profile')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Trivias')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Rankings')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Trivias')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Help')]").click()




#  driver.find_element_by_class_name("btn btn-info")
#  driver.find_element_by_xpath("//*[contains(text(), 'User Profile')]").click()
