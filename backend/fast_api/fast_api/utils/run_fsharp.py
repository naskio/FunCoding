import pyperclip
import fire
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

TO_BE_REPLACED = "Microsoft (R) F# Compiler version 10.2.3 for F# 4.5\nCopyright (c) Microsoft Corporation. All Rights Reserved.\n"

EXAMPLE = """open System
module Main =
    Console.Write("What's your name? ")
    let name = Console.ReadLine()
    Console.Write("Hello, {0}\\n", name)
    Console.WriteLine(System.String.Format("Big Greetings from {0} and {1}", "TutorialsPoint", "Absoulte Classes"))
    Console.WriteLine(System.String.Format("|{0:yyyy-MMM-dd}|", System.DateTime.Now))
"""


# TODO: in progress

def run_code() -> tuple[bool, str]:
    # browser = webdriver.Remote("http://selenium-chrome:4444/wd/hub", DesiredCapabilities.CHROME)
    # browser = webdriver.Chrome()
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # step 1: opening the browser
    browser.get('https://onecompiler.com/fsharp')
    # WebDriverWait(browser, 20).until(ex_cond.element_to_be_clickable((By.ID, 'code'))).click()
    # time.sleep(1)
    print(browser.title, '->', browser.current_url)
    code_area = browser.find_element(By.ID, 'code')
    stdin_area = browser.find_element(By.NAME, 'stdin')
    execute_button = browser.find_element(By.XPATH, "//*[@data-icon='play']")
    # step 2: clearing the code area
    pyperclip.copy(EXAMPLE)

    actions = ActionChains(browser)
    actions.send_keys_to_element(code_area, Keys.CONTROL + "a")
    actions.send_keys_to_element(code_area, Keys.CONTROL + "v")
    actions.perform()
    # for i in range(0, 5):
    #     actions.send_keys_to_element(code_area, Keys.BACKSPACE)
    # actions.perform()

    # actions.send_keys_to_element(code_area, Keys.CONTROL + "a")
    # actions.send_keys_to_element(code_area, Keys.DELETE)
    # actions.perform()
    # actions.send_keys_to_element(code_area, Keys.CONTROL, "v")
    # actions.perform()
    # step 3: writing the code line by line
    # for line in filter(lambda x: x, EXAMPLE.split('\n')):
    #     print('line', line)
    #     # actions = ActionChains(browser)
    #     actions.send_keys_to_element(code_area, line)
    #     actions.perform()
    #     actions.send_keys_to_element(code_area, Keys.ENTER)
    #     actions.perform()
    #     actions.send_keys_to_element(code_area, Keys.CONTROL + Keys.SHIFT + Keys.ARROW_LEFT)
    #     actions.send_keys_to_element(code_area, Keys.DELETE)
    #     actions.perform()
    # step 4: writing the input
    # actions = ActionChains(browser)
    actions.send_keys_to_element(stdin_area, 'Mehdi')
    actions.perform()
    # step 5: executing the code
    # actions = ActionChains(browser)
    actions.click(execute_button)
    actions.perform()
    # step 6: waiting for the output

    # WebDriverWait(browser, 10).until(ex_cond.presence_of_element_located(
    #     (By.ID, "code")
    # ), 'Timed out waiting for Code Editor.')
    # browser.implicitly_wait(1)
    # step 2
    # browser.find_element(By.ID, 'code').send_keys(EXAMPLE)
    # code_area = browser.find_element(By.ID, 'code')
    # code_area = browser.find_element(By.CLASS_NAME, 'ace_text-input')
    # browser.actions.send_keys(EXAMPLE)
    # step 3
    # browser.find_element(By.NAME, 'stdin').send_keys('Mehdi')
    # stdin_area = browser.find_element(By.NAME, 'stdin')
    # step 4
    # browser.find_element(By.XPATH, "//*[@data-icon='play']").click()
    # execute_button = browser.find_element(By.XPATH, "//*[@data-icon='play']")

    # actions = ActionChains(browser)
    # actions.click(code_area)
    # actions.send_keys(EXAMPLE)
    # clearing the code area
    # actions.send_keys_to_element(code_area, Keys.CONTROL + "a")
    # actions.send_keys_to_element(code_area, Keys.DELETE)
    # send line by line

    # actions.send_keys_to_element(stdin_area, 'Mehdi')
    # actions.click(execute_button)
    # actions.perform()
    # step 5
    # browser.implicitly_wait(10)
    # step 6
    # WebDriverWait(browser, 10).until(
    #     ex_cond.presence_of_element_located((By.ID, 'output'))
    # )

    # if 'erreur' in browser.title:
    #     return False, f'Page error: "{browser.title}"'
    # browser.get("https://rdv-etrangers-94.interieur.gouv.fr/")
    # browser.find_element(By.ID, 'CPId').send_keys("94250" + Keys.RETURN)
    # # step 2
    # browser.implicitly_wait(2)
    # print(browser.title, '->', browser.current_url)
    # if 'erreur' in browser.title:
    #     return False, f'Page error: "{browser.title}"'
    # browser.find_element(By.XPATH, "//*[@name='selectedMotiveKeyList'][@value='20']").click()
    # browser.find_element(By.ID, 'nextButtonId').click()
    # # check alert
    # try:
    #     WebDriverWait(browser, 10).until(ex_cond.alert_is_present(), 'Timed out waiting for alert.')
    #     alert = browser.switch_to.alert
    #     if alert.text == "Il n'y a pas de rendez-vous disponible pour ce service.":
    #         browser.quit()
    #         return False, "Alert found"
    #     alert.accept()  # alert accepted
    # except TimeoutException:  # alert not detected
    #     pass
    # # step 3
    # print(browser.title, '->', browser.current_url)
    # if 'erreur' in browser.title:
    #     return False, f'Page error: "{browser.title}"'
    # # day_input = browser.find_element(By.ID, 'dayValueId')  # id=dayValueId or name=dayValue
    # # hour_input = browser.find_element(By.NAME, 'hourValue')  # name=hourValue
    # day_input = WebDriverWait(browser, 10).until(
    #     ex_cond.presence_of_element_located((By.ID, "dayValueId"))
    # )
    # if not day_input.is_enabled():
    #     browser.quit()
    #     return False, "input(id='dayValueId') is disabled"
    # browser.quit()
    time.sleep(10)
    return True, "RDV available !"


if __name__ == '__main__':
    run_code()
