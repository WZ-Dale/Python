# @License : 西安工业大学
# @Author  : 王泽 WZ-Dale
# @Time    : 2021/6/24 11:16

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains    # 事件链
from selenium.webdriver.chrome.options import Options
from chaojiying import Chaojiying_Client
import time

# 允许自动化控制
# Chrome的版本大于88的：
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')        # 允许自动化控制

web = Chrome(options=option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(3)
# 先处理验证码
chaojiying = Chaojiying_Client('账号', '密码', '软件ID')
verify_img_element = web.find_element_by_xpath('//*[@id="J-loginImg"]')
dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
result = dic['pic_str']        # x1,y1|x2,y2|x3,y3
rs_list = result.split("|")
for rs in rs_list:
    p_temp = rs.split(",")
    x = int(p_temp[0])
    y = int(p_temp[1])
    # 要让鼠标移动到某个位置，然后点击，在定义好了事件链之后，开始执行动作perform()
    ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform()
time.sleep(1)
# 填账号、密码、验证码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('账号')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('密码')
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(1)
# 拖拽滑块
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()

