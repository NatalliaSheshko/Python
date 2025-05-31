import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Kalkpro(unittest.TestCase):
    # https://kalk.pro/finish/wallpaper/
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # открытие страницы при начале каждого теста
        self.driver.get('https://kalk.pro/finish/wallpaper/')
        self.driver.implicitly_wait(15)


    def acceptButton(self):
        driver = self.driver
        #button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PATH, "//button [contains(text(), 'Принимаю соглашение')]")))
        button = driver.find_element(By.PATH, "//button [contains(text(), 'Принимаю соглашение')]")
        button.click()

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    # вспомогательный метод для заполнения размеров комнаты
    def input_walls_data(self, hei, wid, len):
        driver = self.driver
        # высота
        # находим элемент страницы по ID
        elem = driver.find_element(By.ID, "js--roomСeiling_height")
        # очищаем элемент от старого значения
        elem.clear()
        # вносим новое значение
        elem.send_keys(hei)
        # ширина
        elem = driver.find_element(By.ID, "js--roomSizes_width")
        elem.clear()
        elem.send_keys(wid)
        # длина
        elem = driver.find_element(By.ID, "js--roomSizes_length")
        elem.clear()
        elem.send_keys(len)

    # метод для проверки работы калькулятора при различных
    # размерах комнаты, в т. ч. проверка отображения ошибок
    # при вводе некорректных данных

    def test_walls(self):
        driver = self.driver
        # пробуем ввести размер 1х1х1
        self.input_walls_data(1, 1, 1)
        # запускаем расчет
        elem = driver.find_element(By.CLASS_NAME, "js--calcModelFormSubmit")
        driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.click()
        time.sleep(4)
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь четырех стех размером 1х1 равна 4
        elem = driver.find_element(By.CSS_SELECTOR,
                                   "ul.data-list li:nth-child(4) strong")
        self.assertEqual('4 м²', elem.text)

        # пробуем ввести размер 0х1х1
        self.input_walls_data(0, 1, 1)
        # запускаем расчет
        elem = driver.find_element(By.CLASS_NAME, "js--calcModelFormSubmit")
        elem.click()
        time.sleep(4)
        # проверяем наличие сообщения об ошибке
        self.assertIn('Ошибки', driver.page_source)
        # проверяем наличие одной ссылки на поле ввода
        elems = driver.find_elements(
            By.CSS_SELECTOR, "a.js--onclick-goToField")
        self.assertEqual(len(elems), 1)

        # пробуем ввести размер aхbхc (буквы вместо цифр)
        self.input_walls_data('a', 'b', 'c')
        # запускаем расчет
        elem = driver.find_element(By.CLASS_NAME, "js--calcModelFormSubmit")
        elem.click()
        time.sleep(4)
        # проверяем наличие сообщения об ошибке
        self.assertIn('Ошибки', driver.page_source)
        # проверяем наличие трех ссылок на поля ввода
        elems = driver.find_elements(
            By.CSS_SELECTOR, "a.js--onclick-goToField")
        self.assertEqual(len(elems), 3)

# метод для проверки работы калькулятора
    # при добавлении окон и дверей
    def test_windows(self):
        driver = self.driver
        # пробуем ввести размер 1х1х1
        self.input_walls_data(1, 1, 1)
        # добавляем окно
        elem = driver.find_element(By.CSS_SELECTOR,
                                   "fieldset[name=windows] button")
        elem.click()
        # задаем размеры окна 1х1 - во всю стену, кол-во окон - 1
        elem = driver.find_element(By.ID, "js--windows_height_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element(By.ID, "js--windows_width_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element(By.ID, "js--windows_count_0")
        elem.clear()
        elem.send_keys(1)
        # запускаем расчет
        elem = driver.find_element(By.CLASS_NAME, "js--calcModelFormSubmit")
        driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.click()
        time.sleep(4)
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь трех стен размером 1х1 равна 3
        elem = driver.find_element(By.CSS_SELECTOR,
                                   "ul.data-list li:nth-child(4) strong")
        self.assertEqual('3 м²', elem.text)

        # добавляем дверь
        elem = driver.find_element(By.CSS_SELECTOR,
                                   "fieldset[name=doors] button")
        elem.click()
        # задаем размеры двери 1х1 - во всю стену, кол-во дверей - 1
        elem = driver.find_element(By.ID, "js--doors_height_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element(By.ID, "js--doors_width_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element(By.ID, "js--doors_count_0")
        elem.clear()
        elem.send_keys(1)
        # запускаем расчет
        elem = driver.find_element(By.CLASS_NAME, "js--calcModelFormSubmit")
        elem.click()
        time.sleep(4)
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь двух стен размером 1х1 равна 2
        elem = driver.find_element(By.CSS_SELECTOR,
                                   "ul.data-list li:nth-child(4) strong")
        self.assertEqual('2 м²', elem.text)

    # тестируем кнопочный калькулятор
    def test_calc(self):
        driver = self.driver
        # открываем калькулятор
        elem = driver.find_element(By.CSS_SELECTOR, ".js--onclick-callCalc")
        elem.click()
        # ждем, пока калькулятор откроется
        time.sleep(5)
        # перебираем цифры от 0 до 9 (ноль не будет отображаться перед 1)
        for i in range(10):
            print("Нажатие кнопки ", str(i), ": ")
            elem = driver.find_element(By.NAME, str(i))
            elem.click()
            print("OK")
        # проверяем изображение на дисплее
        # (ноль не будет отображаться перед 1)
        elem = driver.find_element(By.CLASS_NAME, "display-indicator-ceils")
        self.assertEqual(elem.text, '123456789')


if __name__ == '__main__':
    unittest.main()

