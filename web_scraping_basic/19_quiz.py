from selenium import webdriver
import time

browser = webdriver.Chrome()

# 1. 네이버로 이동
browser.get("https://ticket.melon.com/main/index.htm")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("btn_g_login")
elem.click()

elem = browser.find_element_by_class_name("btn_gate.melon")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("xue0903")
browser.find_element_by_id("pwd").send_keys("nhkm1998&ver")

# 4. login 버튼 클릭
browser.find_element_by_id("btnLogin").click()

elem = browser.find_element_by_class_name("btn_gnb_menu.btn_gnb.btn_g_menu02")
elem.click()

elem = browser.find_element_by_id("GENRE_CON_IDOL")
elem.click()

elem = browser.find_element_by_link_text("웨스트브릿지 라이브홀")
elem.click()
# time.sleep(3)

# 5. id를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
# print(browser.page_source)

# 7. 브라우저 종료
# browser.quit()
