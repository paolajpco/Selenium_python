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
driver.maximize_window()
time.sleep(t)

# Campos Form registro
driver.find_element_by_xpath(
    "//input[@placeholder='Escribe tu nombre' and @class='controller__input px-4 w-full h-12']").send_keys("Dana")
time.sleep(t)
driver.find_element_by_xpath(
    "//input[@placeholder='Escribe tu primer apellido']").send_keys("Peña")
time.sleep(t)
# Campo Select tipo documento
try:
    selectTypeId = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "(//select[@aria-label='select-field'])[2]")))
    typeId = Select(selectTypeId)
    typeId.select_by_value("3")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
    time.sleep(4)
driver.find_element_by_xpath(
    "//input[@placeholder='1234567890']").send_keys("95120112016")
time.sleep(t)
driver.find_element_by_xpath(
    "//input[@placeholder='Escribe tu correo electrónico']").send_keys("test@gmail.com")
time.sleep(t)
driver.find_element_by_xpath(
    "//input[@placeholder='Escribe tu teléfono de contacto']").send_keys("3123900046")
time.sleep(t)
driver.find_element_by_xpath(
    "//input[@placeholder='Escribe tu contraseña']").send_keys("Pass123!")
time.sleep(t)
driver.find_element_by_xpath(
    "//input[@placeholder='Confirma tu contraseña']").send_keys("Pass123!")
time.sleep(6)

# Campo Checkbox Acepto politica tratamiento de datos
btn1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@type='checkbox']")))
btn1.click()
time.sleep(6)

# Boton Crear Cuenta
try:
    Btn2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@aria-label='Crear Cuenta']"))).click()

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
time.sleep(t)
wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

# driver.switch_to_alert().accept()  # ejecutar el boton Aceptar

# driver.close()
