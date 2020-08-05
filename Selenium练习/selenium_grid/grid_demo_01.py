from selenium.webdriver import Remote, DesiredCapabilities

# 引用Chrome浏览器配置
driver = Remote(command_executor='http://192.168.124.1:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get("http://www.baidu.com")
# ……
driver.quit()


#java -jar selenium-server-standalone-3.141.59.jar -role node -port 5555
#java -jar selenium-server-standalone-3.141.59.jar -role node -port 5556
