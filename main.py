from selenium import webdriver
import time

if __name__ == '__main__':
    n = 0
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('-ignore-certificate-errors')
        # chrome_options.add_argument('--headless')# 开启的话进入无页面模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.binary_location = (r'C:\Users\jack8\AppData\Local\Google\Chrome\Application\chrome.exe')# 用你的电脑上chrome安装地址替换
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('http://spoc.ccnu.edu.cn/starmoocHomepage')

        driver.find_element_by_id("loginName").clear()
        driver.find_element_by_id("loginName").send_keys("#########")# 输入你的账号替换########
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("########")# 输入你的密码替换########
        driver.find_element_by_id('loginBtn').click()

        time.sleep(1)
        driver.find_element_by_class_name('thumbnail').click()

        time.sleep(1)
        driver.find_element_by_class_name('icon-wmv').click()
        # driver.find_element_by_xpath('//*[@id="test"]/div[2]/div/div[1]/div[1]/a/span').click()
        time.sleep(1200)
        driver.quit()
        n += 1
        print('已完成:%d次'%n)
