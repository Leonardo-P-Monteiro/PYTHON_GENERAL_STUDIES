from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# chrome_options = webdriver.ChromeOptions()
# chrome_browser = webdriver.Chrome(
#     options=chrome_options,
#     )




def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    browser = webdriver.Chrome(
        options=chrome_options,
    )

    return browser


if __name__ == '__main__':
    TIME_WAIT = 10

    # MONTEI MEU BROWSER COM A FUNÇÃO
    options_browser = ()
    browser = make_chrome_browser()
    browser.get('https://www.google.com/')

    # ESPERANDO ENCONTRAR O ELEMENTO INPUT.
    search_input = WebDriverWait(browser, TIME_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello, world!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    link = results.find_elements(By.TAG_NAME, 'a')
    link[0].click()
    

    



    sleep(TIME_WAIT)
