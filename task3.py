from selenium import webdriver
import time
#前程贷
driver=webdriver.Chrome()
driver.get(r"http://8.129.91.152:8765/ ")
driver.maximize_window()
driver.find_element_by_link_text("免费注册").click()
driver.find_element_by_xpath("//*[@id='phone']").send_keys("13872044456") #输入用户名
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click() #点击获取验证码
# 输入验证码
time.sleep(2)
text = driver.find_element_by_xpath('//*[@class="layui-layer-content"]')
str = text.text
a = str[len(str)-4:]
driver.find_element_by_xpath('//*[@name="code"]').send_keys(a)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("1323380020i")#输入密码
driver.find_element_by_xpath("//*[@name='agree']").click()#点击同意服务条款
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()#点击下一步
time.sleep(2)
driver.find_element_by_link_text("系统自动分配").click()#系统自动分配
# data=driver.window_handles
# driver.switch_to.window(data[1])
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a/img").click()#点击实名认证
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[1]/a").click()#点击实名认证
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[1]/div/input').send_keys("张三")
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[2]/div/input').send_keys("42022220001203005X")
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[3]/div/button').click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[4]/a").click()#点击修改密码
driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[2]/div/form/div[1]/input').send_keys("1323380020i")#原密码
driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[2]/div/form/div[2]/input').send_keys("1323380020ii")#新密码
driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[2]/div/form/div[3]/input').send_keys("1323380020ii")#确认密码
driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[2]/div/form/div[5]/button[1]').click()#点击确定
time.sleep(5)
driver.quit()











