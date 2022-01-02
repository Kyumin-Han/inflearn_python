from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://m-flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 29, 30일 선택
browser.find_elements_by_link_text("30")[0].click()