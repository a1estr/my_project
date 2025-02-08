import pytest
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

DOWNLOAD_DIR = "D:\TeachMeSkills\Dev\my_project\lesson21_hw"
FILE_NAME = "file-sample_150kB.pdf"


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
    options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True
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
    scroll_to_element(driver, alert_button1)
    alert_button1.click()
    alert1 = driver.switch_to.alert
    assert alert1.text == "You clicked a button", "Появился неправильный аллерт"
    alert1.accept()

    # Проверка подтверждающего алерта и отмена его
    alert_button2 = driver.find_element(By.ID, "confirmButton")
    scroll_to_element(driver, alert_button2)
    alert_button2.click()
    alert2 = driver.switch_to.alert
    assert alert2.text == "Do you confirm action?", "Появился неправильный аллерт"
    alert2.dismiss()

    # Проверка prompt-алерта и ввод текста
    alert_button3 = driver.find_element(By.ID, "promtButton")
    scroll_to_element(driver, alert_button3)
    alert_button3.click()
    alert3 = driver.switch_to.alert
    assert alert3.text == "Please enter your name", "Появился неправильный аллерт"
    alert3.send_keys("Selenium Test")
    alert3.accept()
    result = driver.find_element(By.ID, "promptResult")
    assert "Selenium Test" in result.text, "Введенный текст не совпадает"


def test_task4_1_сapabilities(driver_ru):
    # Проверка запуска браузера на русском языке
    driver_ru.get("https://www.google.com")
    assert driver_ru.execute_script("return navigator.language") == "ru-RU", \
        "Текущий язык браузера не русский"


def test_task4_2_сapabilities(driver_ru):
    # Настроим ожидание
    wait = WebDriverWait(driver_ru, 10)

    # Перейдем на главную страницу
    driver_ru.get("https://file-examples.com")

    # Закроем окно cookie
    close_cookie_window(driver_ru)

    # Перейдем на страницу скачивания документов
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-27"))).click()

    # Если появляется рекламный баннер, то закрываем его
    close_ads(driver_ru)
    assert "index.php/sample-documents-download/" in driver_ru.current_url, \
        "Failed to navigate to documents page"

    # Найдем нужную кнопку для загрузки PDF файла
    search_field = driver_ru.find_element(By.CSS_SELECTOR,
                                          "#table-files_filter > label > input[type=search]"
                                          )
    scroll_to_element(driver_ru, search_field)
    search_field.send_keys("pdf")
    pdf_download = driver_ru.find_element(By.CSS_SELECTOR,
                                          '#table-files > tbody > tr > td.text-right.file-link > a'
                                          )
    wait.until(EC.element_to_be_clickable(pdf_download)).click()
    assert "index.php/sample-documents-download/sample-pdf-download/" in driver_ru.current_url, \
        "Failed to navigate to file page"

    # Выберем размер скачиваемого файла
    select_size_button = driver_ru.find_element(
        By.XPATH,
        "//td[contains(text(), '150 kB')]/following-sibling::td/a"
    )
    scroll_to_element(driver_ru, select_size_button)
    wait.until(EC.element_to_be_clickable(select_size_button)).click()

    # Проверим, что файл скачался
    wait.until(lambda driver: os.path.exists(os.path.join(DOWNLOAD_DIR, FILE_NAME)), "Файл не скачался")


def test_task5_actions(driver):
    driver.get(" https://jqueryui.com/droppable")

    # Перейдем в нужный фрейм
    frame = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(frame)

    # Найдем необходимые элементы для перетаскивания
    element_to_drag = driver.find_element(By.ID, "draggable")
    element_to_drop = driver.find_element(By.ID, "droppable")

    # Совершим перетаскивание
    actions = ActionChains(driver)
    actions.drag_and_drop(element_to_drag, element_to_drop).perform()

    # Проверим, что перетаскивание прошло успешно
    assert "Dropped!" in element_to_drop.text, "Перетаскивание элемента не выполнено"


def close_ads(driver_ru):
    """Перебирает все рекламные iframes, ищет кнопку 'Close' и закрывает рекламу."""
    try:
        # Находим все iframes на странице
        all_iframes = driver_ru.find_elements(By.TAG_NAME, "iframe")
        print(f"Found {len(all_iframes)} iframes on the page.")

        for iframe in all_iframes:
            try:
                iframe_id = iframe.get_attribute("id")
                if not iframe_id or not iframe_id.startswith("aswift"):
                    continue  # Пропускаем не относящиеся к рекламе iframes

                print(f"Trying to switch to iframe: {iframe_id}")
                driver_ru.switch_to.frame(iframe)

                # Проверяем кнопку закрытия сразу в этом iframe
                try:
                    ad_close_button = WebDriverWait(driver_ru, 2).until(
                        EC.element_to_be_clickable((By.ID, "dismiss-button"))
                    )
                    ad_close_button.click()
                    print("Ad banner closed in main iframe.")
                    driver_ru.switch_to.default_content()
                    return  # Выходим из функции сразу

                except Exception:
                    print("No close button found in main iframe, checking nested iframe.")

                # Ищем вложенный iframe с рекламой
                try:
                    nested_iframe = driver_ru.find_element(By.TAG_NAME, "iframe")
                    driver_ru.switch_to.frame(nested_iframe)
                    print("Switched to nested ad_iframe.")

                    # Проверяем кнопку закрытия внутри вложенного iframe
                    ad_close_button = WebDriverWait(driver_ru, 2).until(
                        EC.element_to_be_clickable((By.ID, "dismiss-button"))
                    )
                    ad_close_button.click()
                    print("Ad banner closed in nested iframe.")
                    driver_ru.switch_to.default_content()
                    return  # Выходим из функции сразу

                except Exception:
                    print(f"No ad found in nested iframe of {iframe_id}, switching back.")

            except Exception as e:
                print(f"Error switching to iframe {iframe_id}: {e}")

            finally:
                driver_ru.switch_to.default_content()  # Возвращаемся в основной контент

        print("No ads found in any iframe.")

    except Exception as e:
        print(f"General error while handling ads: {e}")

    finally:
        driver_ru.switch_to.default_content()
        print("Returned to main content.")


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)


def close_cookie_window(driver):
    """Close the cookie banner if present."""
    try:
        cookie_close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-button.fc-cta-consent.fc-primary-button"))
        )
        cookie_close_button.click()
    except Exception:
        print("No cookie banner to close.")
