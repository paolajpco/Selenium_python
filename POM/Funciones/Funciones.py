import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def NavegarLogin(self, Tiempo):
        driver = self.driver
        driver.get("https://staging-zapatoca.miaguila.com/login/")
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return driver

    def NavegarRegistro(self, Tiempo):
        driver = self.driver
        driver.get("https://staging-zapatoca.miaguila.com/registro/?hidecaptcha=true")
        self.driver.maximize_window()
        t = time.sleep(Tiempo)


if __name__ == '__main__':
    unittest.main()
