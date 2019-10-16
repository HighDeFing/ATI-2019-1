from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5000/CrearCategoria.html")

#gestionar categoria
#driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()

#crear categoria
driver.find_element_by_name("name").send_keys("Comiquitas")
driver.find_element_by_name("desc").send_keys("comiquitas de todos los tiempos")
driver.find_element_by_xpath("//button[contains(text(), 'Crear Categoria')]").click()

