from common import method
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = test_data.data['url']
username = test_data.data.get('username')
password = test_data.data.get('password')
key = test_data.data.get('key')

num = method.search_func(driver, url, username, password, key)
if key in num:
    print('单据编码是：{}'.format(num))
else:
    print('用例执行不通过！')