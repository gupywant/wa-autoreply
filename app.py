from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://web.whatsapp.com/")
input('Press something after scanning ')
time.sleep(1) #time limit to sign you in on the wa web.

try:
    while True:
        unreadMsgs = browser.find_elements(By.XPATH,"//span[contains(@aria-label, 'unread message')]")# @aria-label='1 unread message']")
        if not unreadMsgs:
            print("Total unread messages: 0")
        else:
            # selectable-text copyable-text
            # for i, result in unreadMsgs:
            #     print(f"#{i}: {result.text} ({result.get_property('href')})")
            # print("Total unread messages: "+ str(len(unreadMsgs)))
            text = "Hi, I'm busy right now and will reply ASAP. BTW this is an automated message!"
            for msg in unreadMsgs:
                msg.click()
                
                #test read
                messageRead = browser.find_elements(By.XPATH, "//span[contains(@class, 'selectable-text copyable-text')]")
                message = messageRead[-1].text

                time.sleep(5)
                reply = browser.find_element(By.XPATH,"//div[@title='Type a message']")
                reply.clear()
                if message == 'Gupy':
                    reply.send_keys("Ganteng")
                elif message == 'Halo' or message == 'halo':
                    reply.send_keys("Halo!!")
                elif message == 'Karin' or message == 'karin':
                    # reply.send_keys(base64.b64decode("SGFsbw==").decode('utf-8'))
                    reply.send_keys(base64.b64decode("Q2FudGlr").decode('utf-8'))
                elif message == 'Halo':
                    reply.send_keys('Gunawan Ganteng')
                else:
                    reply.send_keys(text)
                time.sleep(2)
                reply.send_keys(Keys.RETURN)
                time.sleep(2)
                # break
                open_menu = browser.find_element(By.XPATH,"//div[@data-testid='conversation-menu-button']")
                open_menu.click()

                close_chat = browser.find_element(By.XPATH,"//div[@aria-label='Close chat']")
                close_chat_parent = close_chat.find_element(By.XPATH, "..")
                close_chat_parent.click()
                time.sleep(2)
except KeyboardInterrupt:
    pass