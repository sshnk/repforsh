import time

def test_languege(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    btn = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary")
    assert btn, f"Something go wrong, pls reboot"
