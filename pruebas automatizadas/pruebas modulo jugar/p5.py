from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5000/CrearCategoria.html")

#gestionar categoria
#driver.find_element_by_xpath("//*[contains(text(), 'Gestionar Categoria')]").click()

#eliminar categoria

driver.find_element_by_xpath("//button[@name='Comiquitas' and text()='eliminar']").click()

#driver.find_element_by_xpath("//button[@name='Comiquitas' and @value='something']").click()
#[text()="Eliminar"]
