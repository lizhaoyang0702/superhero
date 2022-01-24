import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class sumTest(unittest.TestCase):

    def setUp(self) :
        print("加法测试用例开始")

    def test_sum1(self):
        browser = webdriver.Chrome()

        browser.get("https://www.baidu.com")
        browser.maximize_window()
        time.sleep(5)
        #browser.find_element(By.ID, "1").click()

        #browser.refresh()

        browser.find_element(By.ID, "kw").send_keys("计算器")

        browser.find_element(By.ID, "su").click()
        time.sleep(5)

        #browser.refresh()
        #time.sleep(5)
        #browser.find_element(By.ID, "kw").send_keys("kuangyahe")

        #browser.find_element_by_xpath("//*[@id='content_left']/div[3]/div/div/div/div/div/div/div[1]/h3/div/a")
        browser.find_element(By.XPATH,"//*[@id='1']/div/div/div/div/div[2]/div[2]/span[1]").click()

        browser.find_element(By.XPATH,"//*[@id='1']/div/div/div/div/div[2]/div[5]/span[4]").click()
        #3
        browser.find_element(By.XPATH,"//*[@id='1']/div/div/div/div/div[2]/div[4]/span[3]").click()
        browser.find_element(By.XPATH,"//*[@id='1']/div/div/div/div/div[2]/div[5]/span[3]").click()
        text = browser.find_element(By.XPATH,"//*[@id='1']/div/div/div/div/div[1]/p[2]").text
        self.assertEqual(text,"10")

        #browser.find_element_by_class_name("在线计算器").click()

        time.sleep(5)



        browser.quit()

    def tearDown(self) :
        print("加法测试用例结束")
