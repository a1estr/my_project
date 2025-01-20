import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()


def test_task1_fill_field(driver):
    driver.get("https://omayo.blogspot.com")
    textbox = driver.find_element(By.ID, "textbox1")
    textbox.clear()
    textbox.send_keys("Selenium Test")
    assert textbox.get_attribute("value") == "Selenium Test", \
        "Введенный текст в поле 'Text Box' не совпадает"


def test_task2_dropdown(driver):
    driver.get("https://omayo.blogspot.com")
    dropdown_combobox = Select(driver.find_element(By.ID, "drop1"))
    dropdown_combobox.select_by_visible_text("doc 3")
    assert dropdown_combobox.first_selected_option.text == "doc 3", \
        "Выбран неправильный элемент из выпадающего списка"


def test_task3_tables(driver):
    driver.get("https://demoqa.com/webtables")
    add_new_button = driver.find_element(By.ID, "addNewRecordButton")
    driver.execute_script("arguments[0].scrollIntoView();", add_new_button)
    add_new_button.click()

    # Проверим отображение формы создания записи
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "registration-form-modal"))
    )
    assert driver.find_element(By.ID, "registration-form-modal").text == "Registration Form", \
        "Форма регистрации не появилась"

    # Заполнение формы для создания записи
    driver.find_element(By.ID, "firstName").send_keys("Jhon")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("jhon.doe@example.com")
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "salary").send_keys("50000")
    driver.find_element(By.ID, "department").send_keys("IT")
    driver.find_element(By.ID, "submit").click()

    # Проверка, что запись была добавлена
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "registration-form-modal"))
    )
    table_rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert any("Jhon" in row.text for row in table_rows), \
        "Запись с именем Jhon не была создана"

    # Редактирование записи
    for row in table_rows:
        if "Jhon" in row.text:
            edit_button = row.find_element(By.CLASS_NAME, "mr-2")
            driver.execute_script("arguments[0].scrollIntoView();", edit_button)
            edit_button.click()
            break
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "registration-form-modal"))
    )
    age_field = driver.find_element(By.ID, "age")
    age_field.clear()
    age_field.send_keys("35")
    salary_field = driver.find_element(By.ID, "salary")
    salary_field.clear()
    salary_field.send_keys("55000")
    driver.find_element(By.ID, "submit").click()

    # Проверка, что запись была отредактирована
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "registration-form-modal"))
    )
    edited_table_rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert any("35" and "55000" in row.text for row in edited_table_rows), \
        "Изменения не были внесены в таблицу"

    # Удаление записи
    for row in table_rows:
        if "Jhon" in row.text:
            delete_button = row.find_element(By.CSS_SELECTOR, 'span[title="Delete"]')
            driver.execute_script("arguments[0].scrollIntoView();", delete_button)
            delete_button.click()
            break

    # Проверка, что запись была удалена
    delete_table_rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    assert any("Jhon" not in row.text for row in delete_table_rows), \
        "Запись не была удалена"


def test_task4_serials_search(driver):
    driver.get("http://seasonvar.ru/")
    driver.find_element(By.CLASS_NAME, "headblock-search-txt").send_keys("Castle")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверим, что перешли на страницу с результатами поиска
    assert "Castle" in driver.current_url, \
        "Не удалось открыть страницу с результатами поиска"

    # Проверим, что результат поиска верный
    search_result = driver.find_element(By.CLASS_NAME, "pgs-search-title")
    assert search_result.text == 'Найдено по запросу «Castle»: 26', \
        "Результат поиска неверный"

    # Найдем сериал Касл в результатах поиска и перейдем на страницу сериала
    list_with_serials = driver.find_elements(By.CLASS_NAME, "pgs-search-wrap")
    for serial in list_with_serials:
        title = serial.find_element(By.CSS_SELECTOR, ".pgs-search-info a").text
        if title.strip() == "Касл":
            castle_serial = serial.find_element(By.CSS_SELECTOR, "a.pst")
            driver.execute_script("arguments[0].scrollIntoView();", castle_serial)
            castle_serial.click()
            break

    # Проверим, что нужная страница с сериалом открылась
    serial_name = driver.find_element(By.CLASS_NAME, "pgs-sinfo-title")
    assert "Castle" in serial_name.text, "Некорректная страница с сериалом"
