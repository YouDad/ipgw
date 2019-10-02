USERNAME=""
PASSWORD=""

print(r'from selenium import webdriver')
from selenium import webdriver
print(r'import time')
import time
print(r'import winreg')
import winreg

print(r'desktop_path = winreg.QueryValueEx( winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"), "Desktop")[0]')
desktop_path = winreg.QueryValueEx( winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"), "Desktop")[0]

print(r'browser = webdriver.PhantomJS()')
browser = webdriver.PhantomJS()
print(r'browser.maximize_window()')
browser.maximize_window()

try:
    print(r'browser.get("https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D3")')
    browser.get("https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D3")

    print(r'browser.find_element_by_id("un").send_keys(USERNAME)')
    browser.find_element_by_id("un").send_keys(USERNAME)
    print(r'time.sleep(0.1)')
    time.sleep(0.1)
    print(r'browser.find_element_by_id("pd").send_keys(PASSWORD)')
    browser.find_element_by_id("pd").send_keys(PASSWORD)
    print(r'time.sleep(0.1)')
    time.sleep(0.1)
    print(r'browser.find_element_by_id("index_login_btn").click()')
    browser.find_element_by_id("index_login_btn").click()

    print(r'while browser.find_element_by_id("sum_bytes").text == "":')
    while browser.find_element_by_id("sum_bytes").text == "":
        print(r'time.sleep(0.1)')
        time.sleep(0.1)
    print(r'browser.save_screenshot("%s\\ipgw.png" % desktop_path)')
    browser.save_screenshot("%s\\ipgw.png" % desktop_path)
    print(r'time.sleep(1)')
    time.sleep(1)
except Exception as e:
    print(r'browser.save_screenshot("%s\\ipgw.png" % desktop_path)')
    browser.save_screenshot("%s\\ipgw.png" % desktop_path)
    print(r'time.sleep(1)')
    time.sleep(1)
