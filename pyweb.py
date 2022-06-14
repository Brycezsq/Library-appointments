from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
# 用selenium打开网页
from selenium.webdriver.common.by import By

data = {
    'name': "张全蛋",
    'id': '15722200000000000',
    'phone': '15011111111',
    'street': '昭君街道',
    'village': '新建居委会',
    'personNum': '4',
}

xpath = {
    'image': '/html/body/div/div/div/div[1]/ul/li[3]/span/img',
    'name': '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/input',
    'id': '/html/body/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/input',
    'phone': '/html/body/div[1]/div/div/div[2]/div[1]/div[4]/div[2]/div/input',
    'region': '/html/body/div[1]/div/div/div[2]/div[1]/div[5]/div[2]/div/input',
    'province': "//li[text()='内蒙古自治区']",
    'city1': "/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[2]/ul/li[1]",
    'city2': "/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[2]/ul/li[2]",
    'city3': "/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[2]/ul/li[3]",
    'city4': "/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[2]/ul/li[4]",
    'city5': "/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div/div[2]/div[2]/ul/li[5]",
    'city': "//li[text()='鄂尔多斯市']",
    'county': "//li[text()='达拉特旗']",
    'street': '/html/body/div[1]/div/div/div[2]/div[1]/div[6]/div[2]/div/input',
    'village': '/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div[2]/div/input',
    'personNum': '/html/body/div[1]/div/div/div[2]/div[1]/div[15]/div[2]/div/input',
    'check': '/html/body/div[1]/div/div/div[2]/div[1]/div[7]/div/div[1]/button[2]',
    'button1': '/html/body/div[1]/div/div/div[2]/div[1]/div[14]/div/div/div/div/div[2]/div/i',
    'button2': '/html/body/div[1]/div/div/div[2]/div[1]/div[16]/div/div/div/div/div[2]/div/i',
    'button3': '/html/body/div[1]/div/div/div[2]/div[1]/div[19]/div/div/div/div/div[1]/div/i',
    'submit': '//html/body/div[1]/div/div/div[2]/div[2]/button',
    'order': ".//*[text()='预约']/..",
}


def fillForm(driver):
    # 姓名
    driver.find_element(By.XPATH, xpath['name']).send_keys(
        data['name'])

    # 身份证号
    driver.find_element(By.XPATH, xpath['id']).send_keys(
        data['id'])

    # 手机号填写
    driver.find_element(By.XPATH, xpath['phone']).send_keys(
        data['phone'])

    # 街道填写
    driver.find_element(By.XPATH, xpath['street']).send_keys(
        data['street'])

    # 小区填写
    driver.find_element(By.XPATH, xpath['village']).send_keys(
        data['village'])

    # 地区选择
    driver.find_element(By.XPATH, xpath['region']).click()

    # 省选择
    is_visible(driver, xpath['province'])
    move = driver.find_element(By.XPATH, xpath['province'])
    ActionChains(driver).move_to_element(move).perform()

    # 市选择 有点恶心
    is_visible(driver, xpath['city2'])
    move = driver.find_element(By.XPATH, xpath['city2'])
    ActionChains(driver).move_to_element(move).click().perform()
    is_visible(driver, xpath['city4'])
    move = driver.find_element(By.XPATH, xpath['city4'])
    ActionChains(driver).move_to_element(move).click().perform()
    is_visible(driver, xpath['city'])
    move = driver.find_element(By.XPATH, xpath['city'])
    ActionChains(driver).move_to_element(move).click().perform()

    # 旗县选择
    is_visible(driver, xpath['county'])
    move = driver.find_element(By.XPATH, xpath['county'])
    ActionChains(driver).move_to_element(move).click().perform()

    # 确定地址
    is_visible(driver, xpath['check'])
    driver.find_element(By.XPATH, xpath['check']).click()

    # 近14天是否接触高风险人员
    driver.find_element(By.XPATH, xpath['button1']).click()

    # 近14天是否离开本市
    time.sleep(5)
    driver.find_element(By.XPATH, xpath['button2']).click()

    # 无症状
    driver.find_element(By.XPATH, xpath['button3']).click()

    time.sleep(5)
    driver.find_element(By.XPATH, xpath['submit']).click()


def is_visible(driver, locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False


def openPage():
    driver = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")
    driver.get("http://dj.ggwhy.cn:8033/#/index?orga=dltq")
    is_visible(driver, xpath['image'])
    driver.find_element(By.XPATH, xpath['image']).click()
    time.sleep(10)
    # 预约
    is_visible(driver, xpath['order'])
    driver.find_element(By.XPATH, xpath['order']).click()
    time.sleep(2)
    posturl = driver.current_url
    if posturl == "http://dj.ggwhy.cn:8033/#/info-edit?orga=dltq":
        fillForm(driver)
        time.sleep(100)
    else:
        pass
    print(posturl)


openPage()
