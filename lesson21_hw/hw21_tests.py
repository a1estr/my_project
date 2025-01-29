import pytest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()


@pytest.fixture()
def driver_ru():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--lang=ru")
    download_dir = "D:\TeachMeSkills\Dev\my_project\lesson21_hw"
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir
    })
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()


def test_task1_windows(driver):
    driver.get("https://demoqa.com/browser-windows")

    # Созданим новую вкладку
    driver.find_element(By.ID, "tabButton").click()

    # Переключение на новую вкладку
    opened_handles = driver.window_handles
    driver.switch_to.window(opened_handles[1])
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page", \
        "Текст в открытой вкладке не соответствует"

    # Закроем вкладку и вернемся на исходную
    driver.close()
    driver.switch_to.window(opened_handles[0])
    assert driver.current_window_handle == opened_handles[0], \
        "Исходное окно неактивно"


def test_task2_frames(driver):
    driver.get("https://demoqa.com/frames")

    # Переключимся на первый фрейм и выполним проверку
    driver.switch_to.frame("frame1")
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page", \
        "Текст в выбранной фрейме не совпадает"

    # Переключимся на основную страницу
    driver.switch_to.default_content()

    # Переключимся на второй фрейм и выполним проверку
    driver.switch_to.frame("frame2")
    assert driver.find_element(By.ID, "sampleHeading").text == "This is a sample page", \
        "Текст в выбранной фрейме не совпадает"


def test_task3_alerts(driver):
    driver.get("https://demoqa.com/alerts")

    # Проверка простого алерта и подтверждение его
    alert_button1 = driver.find_element(By.ID, "alertButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button1)
    alert_button1.click()
    alert1 = driver.switch_to.alert
    assert alert1.text == "You clicked a button", "Появился неправильный аллерт"
    alert1.accept()

    # Проверка подтверждающего алерта и отмена его
    alert_button2 = driver.find_element(By.ID, "confirmButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button2)
    alert_button2.click()
    alert2 = driver.switch_to.alert
    assert alert2.text == "Do you confirm action?", "Появился неправильный аллерт"
    alert2.dismiss()

    # Проверка prompt-алерта и ввод текста
    alert_button3 = driver.find_element(By.ID, "promtButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button3)
    alert_button3.click()
    alert3 = driver.switch_to.alert
    assert alert3.text == "Please enter your name", "Появился неправильный аллерт"
    alert3.send_keys("Selenium Test")
    alert3.accept()
    result = driver.find_element(By.ID, "promptResult")
    assert "Selenium Test" in result.text, "Введенный текст не совпадает"


def test_task4_сapabilities(driver_ru):
    driver_ru.get("https://www.google.com")
    assert driver_ru.execute_script("return navigator.language") == "ru-RU", \
        "Текущий язык браузера не русский"

    driver_ru.get("https://file-examples.com")

    # Находим необходимую кнопку для перехода на страницу скачивания документов
    browse_buttons = driver_ru.find_elements(By.CLASS_NAME, "feature-item")
    document_button = None
    for button in browse_buttons:
        title = button.find_element(By.CSS_SELECTOR, "h3").text
        if title == "Documents":
            document_button = button.find_element(By.CSS_SELECTOR, "a.btn")
            break
    driver_ru.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                             document_button
                             )
    document_button = WebDriverWait(driver_ru, 10).until(
        EC.element_to_be_clickable(document_button)
    )
    document_button.click()

    # Если появляется рекламмный баннер, то закрываем его
    wait_banner = WebDriverWait(driver_ru,
                                timeout=5,
                                poll_frequency=2,
                                ignored_exceptions=[TimeoutException]
                                )
    iframe_banner = wait_banner.until(EC.presence_of_element_located((By.ID, "ad_iframe")))
    driver_ru.switch_to.frame(iframe_banner)
    driver_ru.find_element(By.ID, "dismiss-button").click()
    driver_ru.switch_to.default_content()

    # Найдем нужную кнопку для загрузки PDF файла
    search_filter = driver_ru.find_element(By.XPATH,'//*[@id="table-files_filter"]/label/input')
    driver_ru.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                             search_filter
                             )
    search_filter.send_keys("PDF")
    import pdb
    pdb.set_trace()
    document_size_button = None
    for button in document_size_buttons:
        title = button.find_element(By.CLASS_NAME, "file-ext").text
        if title == "PDF":
            document_size_button = button.find_element(By.CSS_SELECTOR, "a.btn")
            break
    driver_ru.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                             document_size_button
                             )
    document_button = WebDriverWait(driver_ru, 10).until(
        EC.element_to_be_clickable(document_size_button)
    )
    document_size_button.click()




def test_task5_actions(driver):
    driver.get(" https://jqueryui.com/droppable")

    # Перейдем в нужный фрейм
    frame = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(frame)

    #Найдем необходимые элементы для перетаскивания
    element_to_drag = driver.find_element(By.ID, "draggable")
    element_to_drop = driver.find_element(By.ID, "droppable")

    # Совершим перетаскивание
    actions = ActionChains(driver)
    actions.drag_and_drop(element_to_drag, element_to_drop).perform()

    # Проверим, что перетаскивание прошло успешно
    assert "Dropped!" in element_to_drop.text, "Перетаскивание элемента не выполнено"
