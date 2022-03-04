import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
t = 2

driver.get("https://staging-zapatoca.miaguila.com/registro/?hidecaptcha=true")

print(driver.title)

driver.maximize_window()
time.sleep(t)

# Campos Form registro
driver.find_element_by_xpath("//input[@placeholder='Escribe tu nombre' and @class='controller__input px-4 w-full h-12']").send_keys("Dana")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Escribe tu primer apellido']").send_keys("Peña")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='1234567890']").send_keys("95120112016")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Escribe tu correo electrónico']").send_keys("paolajpco@gmail.com")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Escribe tu teléfono de contacto']").send_keys("3123900046")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Escribe tu contraseña']").send_keys("Pass123!")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Confirma tu contraseña']").send_keys("Pass123!")
time.sleep(1)

#Campo CheckBox

try:
    selectTypeId = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//select[@class='select__controler'])[2]")))
    typeId=Select(selectTypeId)
    typeId.select_by_visible_text("Cédula de extranjería")
    time.sleep(1)
    typeId.select_by_index(1)
    time.sleep(1)
    typeId.select_by_value("1")
    time.sleep(1)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


driver.find_element_by_xpath("").is_selected(2)
time.sleep(1)



#driver.close()


#Campos Form Login


