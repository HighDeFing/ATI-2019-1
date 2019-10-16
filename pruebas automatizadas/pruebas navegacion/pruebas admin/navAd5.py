from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5000/CrearCategoria.html")

#navegacion admin
#desde help a todos 
element=driver.find_element_by_xpath("//*[contains(text(), 'Trivias')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Admin Profile')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Roles')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Help')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Trivia')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Ganadores')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()
element=driver.find_element_by_xpath("//*[contains(text(), 'Status Primios')]").click()




#  driver.find_element_by_class_name("btn btn-info")
#  driver.find_element_by_xpath("//*[contains(text(), 'User Profile')]").click()
