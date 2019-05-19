from selenium import webdriver
import time
import random

import pytesseract
from PIL import Image

import base64

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
filePath = './pic.png'

def login():
    driver.get('http://spoc.ccnu.edu.cn/starmoocHomepage')
    driver.implicitly_wait(10)
    driver.find_element_by_id("loginName").clear()
    driver.find_element_by_id("loginName").send_keys("2018171143")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("2018171143")
    src = driver.find_element_by_id('verifCodeImg').get_attribute('src').split(',',1)[1]
    img=base64.b64decode(src)
    with open(filePath,'wb') as f:
        f.write(img)
    image_en = Image.open('pic.png')
    text_en = pytesseract.image_to_string(image_en)
    driver.find_element_by_id('verifCode').send_keys(text_en)
    driver.find_element_by_id('loginBtn').click()

def class_chose():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="s-h-course-info"]/div[1]/div').click()
    time.sleep(2)

def switch_close(n):
    print('第%d次开始' % n)
    # time.sleep(2)
    time.sleep(random.randint(600,1200))
    print('第%d次结束' % n)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def time_getter():

    login()

    class_chose()

    button_li1 = driver.find_elements_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div/div/div/div[5]/h4/i')
    for i in button_li1:
        i.click()

    button_li2 = driver.find_elements_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div/div/div/div[5]/div/div/div[1]/h4/i')
    for i in button_li2:
        i.click()

    button_li3 = driver.find_elements_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div/div/div/div[5]/div/div/div[1]/div/div/div/h4/i')
    for i in button_li3:
        i.click()

    button_li4 = driver.find_elements_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div/div/div/div[5]/div/div/div[1]/div/div/div/div/div/div/h4/i')
    for i in button_li4:
        i.click()


    url_li = driver.find_elements_by_xpath('//*[@id="test"]/div/div/div/div/div/div/div/div/div/div[5]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/a/span')
    for n, i in enumerate(url_li):
        i.click()
        switch_close(n + 1)
    driver.quit()

if __name__ == '__main__':
    m = 1
    while True:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('-ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options)

        print('第%d轮循环开始'%m)
        time_getter()
        m += 1
