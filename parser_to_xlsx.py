import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL веб-сайта, который вы хотите парсить
url = 'https://datatables.net/'  # Замените на нужный URL

# Отправка запроса к веб-сайту
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Создание объекта BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Найдите нужную таблицу (например, первую таблицу на странице)
    table = soup.find('table')

    # Инициализация списка для хранения данных
    data = []

    # Обработка строк таблицы
    for row in table.find_all('tr'):
        cols = row.find_all(['td', 'th'])  # Обрабатываем как ячейки данных, так и заголовки
        cols = [col.text.strip() for col in cols]  # Извлечение текста и удаление пробелов
        data.append(cols)

    # Создание DataFrame из данных
    df = pd.DataFrame(data)

    # Сохранение DataFrame в файл Excel
    df.to_excel('output.xlsx', index=False)

    print("Данные успешно сохранены в 'output.xlsx'!")
else:
    print("Ошибка при запросе к сайту. Статус код:", response.status_code)
