from selenium import webdriver
import time
import random
import pytesseract
from PIL import Image
import base64

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"#你需要安装Tesseract，这是默认安装地址
filePath = 'D:\luvm\onedrive\python_class\工具\cnn_class\pic.png'#选一个图片放置位
if __name__ == '__main__':
    xpath_list = ['//*[@id="test"]/div[2]/div/div[1]/div[1]/a/span','//*[@id="test"]/div[2]/div/div[2]/div[1]/a/span','//*[@id="test"]/div[2]/div/div[3]/div[1]/a/span','//*[@id="test"]/div[2]/div/div[4]/div[1]/a/span',
                  '//*[@id="test"]/div[3]/div/div[7]/div[1]/a/span','//*[@id="test"]/div[3]/div/div[8]/div[1]/a/span','//*[@id="test"]/div[3]/div/div[9]/div[1]/a/span','//*[@id="test"]/div[3]/div/div[10]/div[1]/a/span',
                  '//*[@id="test"]/div[4]/div/div[1]/div[1]/a/span','//*[@id="test"]/div[4]/div/div[2]/div[1]/a/span',
                  '//*[@id="test"]/div[5]/div/div[7]/div[1]/a/span','//*[@id="test"]/div[5]/div/div[8]/div[1]/a/span','//*[@id="test"]/div[5]/div/div[9]/div[1]/a/span',
                  '//*[@id="test"]/div[6]/div/div[1]/div[1]/a/span','//*[@id="test"]/div[6]/div/div[2]/div[1]/a/span',
                  '//*[@id="test"]/div[7]/div/div[1]/div[1]/a/span','//*[@id="test"]/div[7]/div/div[2]/div[1]/a/span',
                  '//*[@id="test"]/div[8]/div/div[1]/div[1]/a/span','//*[@id="test"]/div[8]/div/div[2]/div[1]/a/span',
                  '//*[@id="test"]/div[9]/div/div[1]/div[1]/a/span','//*[@id="test"]/div[9]/div/div[2]/div[1]/a/span',]
    m = 1
        while True:
        n = 0
        print('第%d轮循环开始'%m)
        m += 1
        for xpath in xpath_list:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('-ignore-certificate-errors')
            chrome_options.add_argument('--headless')# 注释这条可以检测效果
            chrome_options.add_argument('--disable-gpu')
            chrome_options.binary_location = (r'C:\Users\jack8\AppData\Local\Google\Chrome\Application\chrome.exe')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('http://spoc.ccnu.edu.cn/starmoocHomepage')

            driver.find_element_by_id("loginName").clear()
            driver.find_element_by_id("loginName").send_keys("####")# 输入你的账号到####
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("####")# 输入你的密码到####
            src = driver.find_element_by_id('verifCodeImg').get_attribute('src').split(',',1)[1]
            img=base64.b64decode(src)
            with open(filePath,'wb') as f:
                f.write(img)
            image_en = Image.open('pic.png')
            text_en = pytesseract.image_to_string(image_en)
            driver.find_element_by_id('verifCode').send_keys(text_en)
            driver.find_element_by_id('loginBtn').click()
            
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div/button').click()
            time.sleep(2)
            driver.find_element_by_class_name('thumbnail').click()
            time.sleep(2)
            driver.find_element_by_xpath(xpath).click()

            n += 1
            print('第%d次开始' % n)
            time.sleep(random.randint(600,1800))
            driver.quit()
            print('已完成:%d次' % n)

