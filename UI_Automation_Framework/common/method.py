import time
# 打开浏览器
def open_url(driver,url):
    driver.get(url)
    # 浏览器最大化
    driver.maximize_window()

# 登录
def login_func(driver, username, password):
    # 输入用户名，密码，进行登录操作
    # 输入用户名
    driver.find_element_by_id('username').send_keys(username)
    # 输入密码
    driver.find_element_by_id('password').send_keys(password)
    # 勾选可选项
    driver.find_element_by_xpath("//input[@id = 'rememberUserCode']/following-sibling::ins").click()
    # 点击登录
    driver.find_element_by_id('btnSubmit').click()

def search_func(driver, url, username, password, key):
    open_url(driver,url)
    login_func(driver,username,password)
    # 点击零售出库
    driver.find_element_by_link_text('零售出库').click()
    # 切换iframe
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    id_frame = id_li + '-frame'  # 得到iframe id
    driver.switch_to.frame(id_frame)
    # driver.switch_to.frame(driver.find_element_by_xpath("//xpath[@id='{}']".format(id_frame)))
    # 搜索429
    driver.find_element_by_id('searchNumber').send_keys(key)
    # 点击搜索
    driver.find_element_by_id('searchBtn').click()
    time.sleep(2)
    # 获取单据编码的号码
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num