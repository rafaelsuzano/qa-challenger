
# -*- coding: utf-8 -*-

import time
import unittest
from selenium.webdriver.support.select import Select



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



chrome_options = Options()

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options.add_argument("start-maximized")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--disable-software-rasterizer')

driver =  webdriver.Chrome('C:\\Novatics\\python\\driver\\chromedriver.exe',options=chrome_options) 
driver.maximize_window()
driver.get("https://getlabor.com.br") 
action = ActionChains(driver)


class Test_qa_challenger (unittest.TestCase):

    def test_TU01(self) :
       
        Title_esperado = "Labor - Controle de Horas"
        time.sleep(10)

        print ("Teste Titulo:" + driver.title)
        WebDriverWait(driver, 10).until(
                EC.title_is(driver.title))

        self.assertEqual(driver.title, Title_esperado,"Titulo errado")
        driver.save_screenshot('ScreenShots/test_TU01.png')

       
    def test_TU02(self) :
        Plano =   driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/header/div[2]/section/nav[1]/a[2]")
        action.move_to_element(Plano).perform()  
        driver.save_screenshot('ScreenShots/test_TU02_Plano.png')  
        
        ComoUsar =   driver.find_element(By.XPATH,"//html/body/div[1]/div[1]/div/div/header/div[2]/section/nav[1]/a[3]")
        action.move_to_element(ComoUsar).perform()  
        driver.save_screenshot('ScreenShots/test_TU02_ComoUsar.png')  
        
        Blog =   driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/header/div[2]/section/nav[1]/a[4]")
        action.move_to_element(Blog).perform()  
        driver.save_screenshot('ScreenShots/test_TU02_Blog.png')  

        Entrar =   driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/header/div[2]/section/nav[2]/a[1]")
        action.move_to_element(Entrar).perform()  
        driver.save_screenshot('ScreenShots/test_TU02_Entrar.png')  

    
    def test_TU03(self) :
        
        driver.find_element(By.XPATH, "html/body/div[1]/div[1]/div/div/header/div[2]/section/nav[1]/a[2]").click()
        time.sleep(10)
        driver.save_screenshot('ScreenShots/test_TU03.png')
   
    def test_TU04(self) :
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/header/div[2]/section/nav[2]/a[1]").click()
        driver.find_element(By.XPATH, "/html/body/ui-view/login/div/div/main/section/div/main/form/div[4]/button").click()
      
        Email= driver.find_element(By.XPATH, "/html/body/ui-view/login/div/div/main/section/div/main/form/label/div").text
        Senha= driver.find_element(By.XPATH,"/html/body/ui-view/login/div/div/main/section/div/main/form/div[2]/label/div").text
       
        print("Mensagem de Login obrigatorio:"+ Email)
        print("Mensagem de Senha obrigatorio:"+ Senha)

        driver.save_screenshot('ScreenShots/test_TU04.png')

        self.assertEqual(Email, "Campo obrigatório","Mensagem de campo (Email) obrigatório")
        self.assertEqual(Senha, "Campo obrigatório","Mensagem de campo (Senha) obrigatório")

    def test_TU05(self) :
        nome = "Rafael"
        email = "rafaelsuzano@hotmail.com"
        senha ="1234678"
        time.sleep(10)
        driver.get("https://app.getlabor.com.br/cadastrar") 
       
        
        #Preenchimento de Formulário
        driver.find_element(By.XPATH, "/html/body/ui-view/register/div/div/main/section/div/div[2]/form/label[1]/input").send_keys(nome)
        driver.find_element(By.XPATH,"/html/body/ui-view/register/div/div/main/section/div/div[2]/form/label[2]/select/option[6]").click()
        driver.find_element(By.XPATH,"/html/body/ui-view/register/div/div/main/section/div/div[2]/form/label[3]/input").send_keys(email)
        driver.find_element(By.XPATH,"/html/body/ui-view/register/div/div/main/section/div/div[2]/form/div[2]/label/input").send_keys(senha)
        #Botão Cadastrar).click()
        driver.find_element(By.XPATH,"/html/body/ui-view/register/div/div/main/section/div/div[2]/form/div[3]/button").click()
       
        time.sleep(20)
        driver.save_screenshot('ScreenShots/test_TU05.png')
        #Usuário já cadastrado
        Duplicado= driver.find_element(By.XPATH," /html/body/ui-view/register/div/div/main/section/div/div[2]/form/div[1]").text
        #Dados do Cadastrado Duplicado
        print ("E-mail duplicado :"+email )
        print(Duplicado)
       
        self.assertEqual(Duplicado, Duplicado,"Erro na validação de usuário já cadastrado")
 
    
        
    def test_TU06(self) :
        pass
  
  
  
    def test_TU07(self) :
        email = "rafaelsuzano@hotmail.com"
        senha ="87654321"
        driver.get("https://app.getlabor.com.br/entrar") 

    
        time.sleep(10)
        driver.find_element(By.XPATH,"/html/body/ui-view/login/div/div/main/section/div/main/form/label/input").send_keys(email)
        driver.find_element(By.XPATH,"/html/body/ui-view/login/div/div/main/section/div/main/form/div[2]/label/input").send_keys(senha)
        #Botão Entrar
        driver.find_element(By.XPATH,"/html/body/ui-view/login/div/div/main/section/div/main/form/div[4]/button").click()
        time.sleep(10)
        driver.save_screenshot('ScreenShots/test_TU07.png')
        time.sleep(10)

    def test_TU08(self) : 
       driver.quit()

