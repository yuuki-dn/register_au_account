############################################################
#                  TOOL TẠO TÀI KHOẢN AU                   #
#          Phát triển bởi: June8th a.k.a Lumine <3         #
#       Facebook: https://www.facebook.com/june8th.dan/    #
#           Github: https://github.com/june8th-dan         #
############################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import re
import time
import string
from colorama import Fore,Style
from os import system

# Chế độ ẩn danh
chrome_options = webdriver.ChromeOptions().add_argument('--incognito')

def create_acc_au():
    # Email & Mật khẩu ngẫu nhiên
    rand_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"lumine_{rand_str}@mailforspam.com"
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # Khởi tạo phiên
    session = webdriver.Chrome(chrome_options=chrome_options)
    # Load trang đăng kí tài khoản
    session.get("https://connect.auone.jp/net/vw/cca_eu_net/cca?ID=ENET0510")
    # Đợi trang tải xong
    WebDriverWait(session, 10).until(EC.presence_of_element_located((By.ID, "wowAliasIdEmail")))
    # Step 1
    session.find_element(By.XPATH, '//input[@id="wowAliasIdEmail"]').send_keys(email)
    session.find_element(By.XPATH, '//button[@class="idk-button-primary idk-margin"]').click()
    # Step 2
    WebDriverWait(session, 10).until(EC.presence_of_element_located((By.ID, "confirmcode")))
    # Mở mailforspam.com lấy code
    time.sleep(6)
    session.execute_script(f'window.open("https://mailforspam.com/mail/{email.split("@")[0]}/1","_blank");')
    session.switch_to.window(session.window_handles[1])
    mail_content = session.find_element(By.XPATH, '//p[@id="messagebody"]').text
    code = re.search(r'\b\d{6}\b', mail_content).group()
    session.close()
    session.switch_to.window(session.window_handles[0])
    session.find_element(By.XPATH, '//input[@id="confirmcode"]').send_keys(code)
    session.find_element(By.XPATH, '//button[@class="idk-button-primary idk-margin"]').click()
    # Step 3
    WebDriverWait(session, 10).until(EC.presence_of_element_located((By.ID, "password")))
    session.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    session.find_element(By.XPATH, '//input[@id="csBirthdayYYYY"]').send_keys(str(random.randint(1980,2000)))
    dropdown = session.find_element(By.XPATH, '//select[@id="csBirthdayMM" and @name="csBirthdayMM"]')
    dropdown.find_element(By.XPATH, '//option[@value="{}"]'.format(str(random.randint(1,12)).zfill(2))).click()
    session.find_element(By.XPATH, '//input[@id="csBirthdayDD"]').send_keys(str(random.randint(10,28)))
    session.find_element(By.XPATH, '//label[@class="idk-text-16-bold-no-lh radio-gender" and @data-bind="d_eMail1"]').click()
    session.find_element(By.XPATH, '//button[@name="btn_cmp" and @id="btn_cmp"]').click()
    session.quit()
    return {"email": email, "password": password}

# Main
try: system("cls")
except: system("clear")
print(Fore.RED,    " ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n",
      Fore.YELLOW, "┃                  TOOL TẠO TÀI KHOẢN AU                   ┃\n",
      Fore.GREEN,  "┃          Phát triển bởi: June8th a.k.a Lumine <3         ┃\n",
      Fore.CYAN,   "┃       Facebook: https://www.facebook.com/june8th.dan/    ┃\n",
      Fore.BLUE,   "┃           Github: https://github.com/june8th-dan         ┃\n",
      Fore.MAGENTA,"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n",
      Style.RESET_ALL, "\n")

acc_quantity = int(input("Nhập số lượng acc cần tạo: "))
for i in range(acc_quantity):
    print(Fore.RED, f"\n>>> Đang tạo tài khoản thứ {i + 1}", Style.RESET_ALL)
    result = create_acc_au()
    print("------------------------------------------------",
          Fore.GREEN, "\nTạo tài khoản thành công!", Style.RESET_ALL,
          "\nTài khoản:", Fore.CYAN, result["email"], Style.RESET_ALL,
          "\nMật khẩu: ", Fore.YELLOW, result["password"], Style.RESET_ALL,
          "\n------------------------------------------------")