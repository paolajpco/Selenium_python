import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Funciones.Funciones import Funciones_Globales


class TestCasesLogin():
    
    def __init__(self, driver):
        self.driver = driver

    def test_login1(self, name, passw, t, numpru, msg):
        driver = self.driver
        nl = Funciones_Globales(driver)
        nl.NavegarLogin(t)            
        time.sleep(4)   
        nom = driver.find_element_by_xpath("//input[contains(@data-role,'email_textbox')]")
        clave = driver.find_element_by_xpath("//input[contains(@type,'password')]")
        bt = driver.find_element_by_xpath("//button[@aria-label='Ingresar']")
        nom.send_keys(name)
        clave.send_keys(passw)
        bt.click()
        time.sleep(t)
        error = driver.find_element_by_xpath("(//div[@class='alert__text'])[2]").text
        print(msg)
        print(error)
        assert msg == error, "Test Case 1 Login OK!"
        time.sleep(t)

    def test_login2(self, name, passw, t, numpru, msg1, msg2):
        driver = self.driver
        nl = Funciones_Globales(driver)
        nl.NavegarLogin(t)        
        nom = driver.find_element_by_xpath("//input[contains(@data-role,'email_textbox')]")
        clave = driver.find_element_by_xpath("//input[contains(@type,'password')]")
        nom.send_keys(name)
        clave.send_keys(passw + Keys.ENTER)
        time.sleep(t)
        error1 = driver.find_element_by_xpath("//div[@class='input__error text-left text-medium-negative text-xs'][contains(.,'- Debes ingresar un email válido')]").text
        error2 = driver.find_element_by_xpath("//div[@class='input__error text-left text-medium-negative text-xs'][contains(.,'- Campo Requerido')]").text
        print(msg1)
        print(error1)
        assert msg1 == error1
        time.sleep(t)
        print(msg2)
        print(error2)
        assert msg2 == error2, "Test Case 2 Login OK!"
        time.sleep(t)

    def test_login3(self, name, passw, t, numpru, msg1, msg2):
        driver = self.driver
        nl = Funciones_Globales(driver)
        nl.NavegarLogin(t)        
        nom = driver.find_element_by_xpath("//input[contains(@data-role,'email_textbox')]")
        clave = driver.find_element_by_xpath("//input[contains(@type,'password')]")
        nom.send_keys(name + Keys.TAB)
        clave.send_keys(passw + Keys.TAB)
        time.sleep(t)
        error1 = driver.find_element_by_xpath("//div[@class='input__error text-left text-medium-negative text-xs'][contains(.,'- Debes ingresar un email válido')]").text
        error2 = driver.find_element_by_xpath("//div[@class='input__error text-left text-medium-negative text-xs'][contains(.,'- Campo Requerido')]").text
        print(msg1)
        print(error1)
        assert msg1 == error1, "Test Case 3 Login OK!"
        time.sleep(t)
        print(msg2)
        print(error2)
        assert msg2 == error2
        time.sleep(t)

    def test_login4(self, name, passw, t, numpru, msg1, msg2):
        driver = self.driver
        nl = Funciones_Globales(driver)
        nl.NavegarLogin(t)        
        nom = driver.find_element_by_xpath("//input[contains(@data-role,'email_textbox')]")
        clave = driver.find_element_by_xpath("//input[contains(@type,'password')]")
        nom.send_keys(name + Keys.TAB)
        time.sleep(t)
        clave.send_keys("" + Keys.TAB)
        time.sleep(5)
        error1 = driver.find_element_by_xpath("//div[@class='input__error text-left text-medium-negative text-xs'][contains(.,'- Debes ingresar un email válido')]").text
        error2 = driver.find_element_by_xpath("(//div[@class='input__error text-left text-medium-negative text-xs'])[3]").text

        print(msg1)
        print(error1)
        assert msg1 == error1, "Test Case 4 Login OK!"

        time.sleep(t)
        print(msg2)
        print(error2)
        assert msg2 == error2

    def test_login5(self, name, passw, t, numpru, msg1):
        driver = self.driver
        nl = Funciones_Globales(driver)
        nl.NavegarLogin(t)        
        nom = driver.find_element_by_xpath("//input[contains(@data-role,'email_textbox')]")
        clave = driver.find_element_by_xpath("//input[contains(@type,'password')]")
        nom.send_keys(name + Keys.TAB)
        time.sleep(t)
        clave.send_keys(passw + Keys.TAB)
        time.sleep(t)
        text = driver.find_element_by_xpath(
            "").text
        assert msg1 == text, "Test Case 5 Login OK!"
   
def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
