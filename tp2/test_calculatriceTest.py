# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCalculatriceTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def testAddition(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(707, 738)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("15")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '+']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("12")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    assert self.driver.find_element(By.ID, "result").text == "Résultat : 27"
  def testSub(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(707, 738)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("15")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '-']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("12")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    assert self.driver.find_element(By.ID, "result").text == "Résultat : 3"
  def testMul(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(707, 738)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("15")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '*']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("12")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    assert self.driver.find_element(By.ID, "result").text == "Résultat : 180"  
  def testDiv(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(707, 738)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("15")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '/']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("12")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    assert self.driver.find_element(By.ID, "result").text == "Résultat : 1.25" 
  def testDiv(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(707, 738)
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("15")
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '/']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("0")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    assert self.driver.find_element(By.ID, "result").text == "Résultat : Infinity"    
  def testNull(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  
