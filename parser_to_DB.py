import requests
from bs4 import BeautifulSoup
import sqlite3

# 1. Создание базы данных
def create_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items
                      (id INTEGER PRIMARY KEY, title TEXT, price REAL)''')
    conn.commit()
    conn.close()

# 2. Парсинг данных
def parse_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    items = []
    for item in soup.find_all('div', class_='item'):  # Измените класс в соответствии с сайтом
        title = item.find('h2').text  # или другой тег/класс
        price = float(item.find('span', class_='price').text.replace('$', ''))  # Изменить по необходимости
        items.append((title, price))
    return items

# 3. Сохранение данных в БД
def save_to_database(items):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO items (title, price) VALUES (?, ?)', items)
    conn.commit()
    conn.close()

# 4. Основная функция
def main():
    create_database()
    url = 'https://example.com'  # Заменить на URL целевого сайта
    items = parse_website(url)
    save_to_database(items)
    print(f'Сохранено {len(items)} элементов в базу данных.')

if __name__ == "__main__":
    main()
