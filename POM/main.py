import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Funciones.Funciones import Funciones_Globales
from Login import TestCasesLogin
from Resgistro import TestCasesRegister
t = .5


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\Drivers\chromedriver.exe")
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
 
    def testRegister(self):
        driver = self.driver
        r = TestCasesRegister(driver)
        # Test Case Register User all fields
        r.test_Register1("PAOLA", "GOMEZ", "GOMEZ", "1", "1018426726", "paolajpco@gmail.com", "3003333333",
                         "Pass123!", "Pass123!", t, "Bogotá", "Carrera", "167", "65", "86", "Int5 Apto504","No tenemos cobertura en tu zona")
        # Test Case Register User required fields

    def testLogin(self):
        driver = self.driver
        f = TestCasesLogin(driver)
        #Test Case 1:  Login user & pass No match
        f.test_login1("rodrigo", "admin123", t, 1,
                     "Las credenciales proporcionadas no corresponden a un usuario existente.")
        # # test Case 2: Username is required
        # f.test_login2("", "admin123", t, 2,
        #               "- Debes ingresar un email válido", "- Campo Requerido")
        # # test Case 3: Pass is required
        # f.test_login3("rodrigo", "", t, 3,
        #               "- Debes ingresar un email válido", "- Campo Requerido")
        # #test Case 4: Pass & UserName is required
        # f.test_login4(" ", " ", t, 4,
        #               "- Debes ingresar un email válido", "- Campo Requerido")
        # test Case 5: Pass & UserName is Match
        # f.test_login5("TestOK", "TestOK", t, 5, "Ingreso Exitoso")

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
