#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test 
@File    ：multithreading.py
@IDE     ：PyCharm 
@Date    ：2022/1/6 22:18 
"""
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
from selenium import webdriver
import threadpool
import time


def login(text):
    # for i in range(text):
    #     print(i)
    #     time.sleep(1)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_xpath('//*[@id="su"]').click()
    time.sleep(2)
    driver.quit()
    print(text)


# threads = threading.Thread(target=login, name='子线程', daemon=True)  # 创建线程
# threads.start()
# threads.join()  # 阻塞进程，等待主线程执行结束后，非同时进行，上面target的自行完成后再执行线程
#
# for i in range(5):
#     print(threading.current_thread().name, ' main ', i)
#     print(threads.name + ' is alive ', threads.isAlive())
#     time.sleep(1)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=7)
    search = ['钱光耀', '郑艳芝', '钱本峰', 'lala', 'qwr', 'sfa', 'adsfa']
    # for i in search:
    #     task = executor.submit(login, (i))
    #     # result可以获取该任务的执行结果，是阻塞的，不能并发执行
    #     print(task.result())

    all_task = [executor.submit(login, i) for i in search]
    wait(all_task, return_when=FIRST_COMPLETED)
    print('main')

    # for i in as_completed(all_task):
    #     # as_completed等到全部结束后打印每个人物的结果，不会阻塞进程
    #     print(i.result())

    # for s in executor.map(login, search):
    #     print(s)





