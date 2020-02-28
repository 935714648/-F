import time
from selenium import webdriver
import re
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

join=[
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div/div/div[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[5]/div/div/div[2]/span',
]

zhangjie =[
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[1]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[7]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[8]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[9]/div/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[10]/div/span',
]

shiping =[
#第一章第一节1.1.1---1.1.8
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li/ul/div/li[8]/span',
        #2.2.1---2.2.8
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/ul/div/li/ul/div/li/ul/div/li[8]/span',
        #3.3.1-3.3.8
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/ul/div/li/ul/div/li/ul/div/li[8]/span',

    #第一章没有节数1.1----1.8
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li/ul/div/li[8]/span',
        #第二章2.1--2.8
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[2]/ul/div/li[8]/span',
        #第三章3，1-3.8
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[3]/ul/div/li[8]/span',
        #第四章4.1-4.2
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[4]/ul/div/li[8]/span',
        #第五章
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[5]/ul/div/li[8]/span',
        #第六章
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[1]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[2]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[3]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[4]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[5]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[6]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[7]/span',
        '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/div/li[6]/ul/div/li[8]/span',
]


def jiemian():

    window = Tk()
    window.geometry("400x300")
    window.title("网课自动软件V2正式版 QQ:935714648")

    lbl = Label(window, text="登录界面", font=("微软雅黑", 20))
    lbl1 = Label(window, text="账号:", font=("微软雅黑", 17))
    lbl2 = Label(window, text="密码:", font=("微软雅黑", 17))

    E1 = Entry(window)
    E2 = Entry(window)
    def aaa():
        global name
        name = E1.get()
    def bbb():
        global password
        password= E2.get()


    lbl.place(x=150, y=35)

    lbl1.place(x=55, y=100)
    E1.place(x=110, y=107)

    lbl2.place(x=55, y=150)
    E2.place(x=110, y=157)

    B = tk.Button(window, text="输入账号完点第一下",command=aaa)
    B.place(x=262, y=103)

    B1 = tk.Button(window, text="输入密码完点第二下",command=bbb)
    B1.place(x=262, y=153)

    B3 = tk.Button(window, text="第三下登录!!!",command=aa)
    B3.place(x=150, y=200)


    window.mainloop()

def aa():
    url = 'http://study.ahptc.cn:8088/xuexipc/#/login'
    #所选课程的5个课程的链接



    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    #输入账号
    browser.find_elements_by_css_selector('.el-input__inner')[0].send_keys(name)
        #输入密码
    browser.find_elements_by_css_selector('.el-input__inner')[1].send_keys(password)
        #点击登录


    try:
        browser.find_element_by_css_selector('.el-button.login-form.el-button--success').click()
        time.sleep(1)
    except:
        print('账号或密码错误')


    #点击个人中心
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]').click()
    time.sleep(2)
    #拉到最底部
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    # 点击查看更多个人课程
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div[5]/div[3]/a').click()
    time.sleep(2)
#点击所课程
    for i in join:
        time.sleep(3)
        xuewan = browser.find_element_by_xpath(i).text
        browser.find_element_by_xpath(i).click()
        time.sleep(8)
        #获取进度条
        a = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/span[2]').text
        b = int(a[:2])
        if b != 10:
            #点击继续学习

            browser.find_element_by_css_selector('.study-progress .btn').click()
            time.sleep(5)
            # 获取当前有几个小节视频
            jieshu = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div').text
            jieshu1 = jieshu[1:2]
            print('共有' + jieshu1 +'个视频')


            for iiii in zhangjie:
                try:
                    browser.find_element_by_xpath(iiii).click()
                except:
                    pass


            for ii in shiping:
                time.sleep(3)
                try:
                    browser.find_element_by_xpath(ii).click()
                    time.sleep(3)
                    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/span[2]/span').click()
                    time.sleep(5)
                    jindu = browser.find_element_by_css_selector('.el-progress__text').text
                    if jindu[:3] == '100' or jindu[:3] == '10%':
                        continue;
                    else:
                        # 点击开始播放
                        print('开始播放')
                        time.sleep(2)
                        browser.find_element_by_xpath('//*[@id="video-container"]/div/div[5]/div[2]').click()
                        time.sleep(2)
                        js = 'document.querySelector("video").playbackRate = 15.0'
                        try:
                            browser.execute_script(js)
                        except:
                            print('加速出错')
                        time.sleep(2)
                        browser.implicitly_wait(40)
                        try:
                            print('开始验证码')
                            tiqu = browser.find_element_by_css_selector('.el-message-box__message p').text
                            time.sleep(2)
                            print(tiqu)
                            tiqu1 = re.findall('\d+', a)
                            b = int(tiqu1[0])
                            c = int(tiqu1[1])
                            e = (tiqu[5:6])
                            if e == '+':
                                f = b + c
                                print(f)
                            elif e == '-':
                                f = b - c
                                print(f)
                            else:
                                print('出错')
                            browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/input').send_keys(f)
                            browser.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]/span').click()
                            time.sleep(30)
                            continue;
                        except:
                            print('没有发现验证码')
                            time.sleep(30)
                            continue;
                except:
                    print('没有这个视频')
                    continue;

            browser.back()
            browser.back()
        else:
            print('已学完科目报告：'+xuewan)
            browser.back()
            browser.refresh()
            time.sleep(5)
            continue;
    browser.quit()
if __name__ == '__main__':
    jiemian()
