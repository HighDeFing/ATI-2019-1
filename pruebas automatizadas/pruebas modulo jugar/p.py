from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5000/home.html")
driver.find_element_by_xpath("//*[contains(text(), 'Go trivia')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Go trivia')]").click()

#prueba todas las respuestas correctas
driver.find_element_by_id("choiceA").click()

driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'Cerrar')]").click()
driver.find_element_by_id("choiceC").click()
driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'Cerrar')]").click()
driver.find_element_by_id("choiceC").click()
driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'Cerrar')]").click()
driver.find_element_by_id("choiceB").click()
driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'Cerrar')]").click()
driver.find_element_by_id("choiceD").click()
driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'Cerrar')]").click()
driver.find_element_by_id("choiceB").click()
driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'Cerrar')]").click()
driver.find_element_by_id("choiceA").click()
driver.find_element_by_xpath("//*[contains(text(), 'Siguiente')]").click()

driver.find_element_by_xpath("//*[contains(text(), 'iniciar otro juego')]").click()

#  driver.find_element_by_class_name("btn btn-info")
#  driver.find_element_by_xpath("//*[contains(text(), 'User Profile')]").click()
