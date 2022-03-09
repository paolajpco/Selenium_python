import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from Funciones.Funciones import Funciones_Globales


class TestCasesRegister():

    def __init__(self, driver):
        self.driver = driver

# Test Case 1: Register User all fields

    def test_Register1(self, name, Apell, Apell2, TipoDoc, NroDoc, Mail, Tel, passw1, passw2, t, city,dir1,dir2Str,dir3Str,dir4Str,CompDirStr,msgC ):
        driver = self.driver
        nr = Funciones_Globales(driver)
        nr.NavegarRegistro(t)
        nombre = driver.find_element(
            By.XPATH, "//input[contains(@placeholder,'Escribe tu nombre')]")
        #nombre = driver.find_element_by_xpath("//input[contains(@placeholder,'Escribe tu nombre')]")
        Apellido = driver.find_element(
            By.XPATH, "//input[@placeholder='Escribe tu primer apellido']")
        Apellido2 = driver.find_element(
            By.XPATH, "//input[contains(@placeholder,'Escribe tu segundo apellido')]")
        # TipoDoc
        # Campo Select tipo documento
        
        NroDocumento = driver.find_element(
            By.XPATH, "//input[@placeholder='1234567890']")
        EMail = driver.find_element(
            By.XPATH, "//input[@placeholder='Escribe tu correo electrónico']")
        Telefono = driver.find_element(
            By.XPATH, "//input[@placeholder='Escribe tu teléfono de contacto']")
        Clave1 = driver.find_element(
            By.XPATH, "//input[@placeholder='Escribe tu contraseña']")
        Clave2 = driver.find_element(
            By.XPATH, "//input[@placeholder='Confirma tu contraseña']")
        print(":::::::::::::::::::::INGRESE:::::::::::::::::::::")
        time.sleep(t)
        nombre.send_keys(name)
        time.sleep(t)
        Apellido.send_keys(Apell + Keys.ENTER)
        time.sleep(t)
        Apellido2.send_keys(Apell2 + Keys.ENTER)
        time.sleep(t)
        #TipoDoc.send_keys(TipoDoc +Keys.ENTER)
        # time.sleep(t)
        try:
            selectTypeId = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "(//select[@aria-label='select-field'])[2]")))
            typeId = Select(selectTypeId)
            typeId.select_by_value(TipoDoc)
            time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible")
            time.sleep(t)
        NroDocumento.send_keys(NroDoc + Keys.ENTER)
        time.sleep(t)
        EMail.send_keys(Mail + Keys.ENTER)
        time.sleep(t)
        Telefono.send_keys(Tel+Keys.ENTER)
        time.sleep(t)
        Clave1.send_keys(passw1+Keys.ENTER)
        time.sleep(t)
        Clave2.send_keys(passw2+Keys.ENTER)
        driver.execute_script("window.scrollTo(0,600)")
        time.sleep(t)
        # Campo Checkbox Acepto politica tratamiento de datos
        btn1 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='checkbox']")))      
        time.sleep(t)
        btn1.click()
        time.sleep(t)
        # Boton Crear Cuenta
        Btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Crear Cuenta']")))
        Btn2.click()
        time.sleep(t)                
        alert = Alert(driver)       
        alert.accept()
        time.sleep(t)
        ################################
        #FORM DIRECCION
        #Input de ciudad Tipo Combobox
        cityInput = driver.find_element(
            By.XPATH, "(//input[@required='required'])[1]")        
        cityInput.send_keys(city+Keys.ENTER)
        time.sleep(4)
        cityTrash = driver.find_element(
            By.XPATH, "//li[contains(@id,'autocomplete-item-0')]") 
        cityTrash.click()
        time.sleep(t)
        #Select de dir1 Tipo Combobox
        try:
            selectTypeId = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(//select[@class='select__controler'])[1]")))
            typeId = Select(selectTypeId)
            typeId.select_by_value(dir1)
            time.sleep(t)
        except TimeoutException as ex:
            print(ex.msg)

        #Select de dir2 Tipo Input
        dir2 = driver.find_element(
            By.XPATH, "(//input[@aria-label='input-field'])[2]")
        #Select de dir3 Tipo Input
        dir3= driver.find_element(
            By.XPATH, "(//input[@aria-label='input-field'])[3]")
        #Select de dir4 Tipo Input
        dir4 = driver.find_element(
            By.XPATH, "(//input[@required='required'])[4]")
        # SendKeys Form Direccion    
        dir2.send_keys(dir2Str+Keys.ENTER)
        time.sleep(t)
        dir3.send_keys(dir3Str+Keys.ENTER)
        time.sleep(t)
        dir4.send_keys(dir4Str+Keys.ENTER)
        time.sleep(t)
        #Boton Buscar Direccion
        BtonDir= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'BUSCAR Espera...')]")))
        BtonDir.click()
        time.sleep(4)
        # Boton Form seleccionar en el Mapa
        BtonMap= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Seleccionar en el mapa')]")))
        BtonMap.click()
        time.sleep(t)
        # Input Direccion Complemento
        ComplementoDir= driver.find_element(
            By.XPATH, "//input[@tabindex='4']")
        ComplementoDir.send_keys(CompDirStr+Keys.ENTER)
        time.sleep(4)
        # Boton Confirmar
        BtonConfMap= WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Confirmar']")))
        BtonConfMap.click()
        time.sleep(6)     
        # Boton Confirmar
        BtonSecConfMap= WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(.,'Confirmar')])[2]")))
        BtonSecConfMap.click()
        time.sleep(6)     
        # Texto Cobertura Envios
        MsgCobertura= driver.find_element(
            By.XPATH, "//p[contains(.,'No tenemos cobertura en tu zona')]")
        #//p[contains(.,'No tenemos cobertura en tu zona')]
        #Assert Cobertura
        assert msgC == MsgCobertura, "Test Case 1 Register OK!"
        
def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
