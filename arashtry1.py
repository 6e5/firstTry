from splinter import Browser
import time
def start():
    x = input('[+] Post URL: ')
    browser = Browser('chrome')
    # Visit URL
    url = "https://igsub.me"
    url2 = "https://igsub.me/postViews"
    browser.visit(url)
    browser.visit(url2)

    #buttonServer = browser.find_by_value('Get Page (THIS SERVER)').click()

    link = browser.find_by_name('formPostLink').click()
    browser.fill('formPostLink',x)
    # Find and click the 'search' button
    browser.find_by_id('firstFormElementSendButton').click()
    time.sleep(4)

    browser.find_by_name('formPostActionLimit').click()

    count = browser.find_by_value('3000').click()

    send = browser.find_by_id('secondFormElementSendButton').click()


    # Interact with elements
    #button.click()
    while browser.is_text_present('PROCESSING...'):
        print("PROCESSING...")
    else:
        print("Done")
        start()
