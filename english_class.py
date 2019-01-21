from selenium import webdriver
import time
import random

def login():
    driver.get('http://spoc.ccnu.edu.cn/starmoocHomepage')

    driver.find_element_by_id("loginName").clear()
    driver.find_element_by_id("loginName").send_keys("####")#输入你的账号替换####
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("####")#输入你的密码替换####
    driver.find_element_by_id('loginBtn').click()

def class_chose():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/button').click()
    time.sleep(2)
    driver.find_element_by_class_name('border').click()
    time.sleep(2)

def swith_close(n):
    print('第%d次开始' % n)
    # time.sleep(2)
    time.sleep(random.randint(600,1200))
    print('第%d次结束' % n)
    driver.switch_to_window(driver.window_handles[1])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

def time_getter():
    n = 0

    login()

    class_chose()

    list1 = []
    for t in range(1,9):
        if t == 1:
            a = 3
        else:
            a = 2
        if t == 7:
            b = 2
        else:
            b = 1
        driver.find_element_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div[{}]/div/div/div[{}]/h4/i'.format(t,a)).click()
        driver.find_element_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div[{}]/div/div/div[{}]/div/div/div[1]/h4/i'.format(t,a)).click()
        driver.find_element_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div[{}]/div/div/div[{}]/div/div/div[1]/div/div/div[{}]/h4/i'.format(t,a,b)).click()
        list2 = driver.find_elements_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div[{}]/div/div/div[{}]/div/div/div[1]/div/div/div[{}]/div/div/div/h4/i'.format(t,a,b))
        for i,li in enumerate(list2,1):
            li.click()
            li.find_element_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div[{}]/div/div/div[{}]/div/div/div[1]/div/div/div[{}]/div/div/div[{}]/div/div/div[1]/a/span'.format(t,a,b,i)).click()
            n += 1
            swith_close(n)
    driver.quit()

if __name__ == '__main__':
    m = 1
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('-ignore-certificate-errors')
        # chrome_options.add_argument('--headless')#进入无页面模式请取消注释
        chrome_options.add_argument('--disable-gpu')
        chrome_options.binary_location = (r'C:\Users\jack8\AppData\Local\Google\Chrome\Application\chrome.exe')
        driver = webdriver.Chrome(options=chrome_options)

        print('第%d轮循环开始'%m)
        time_getter()
        m += 1
