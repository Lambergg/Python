import requests
from bs4 import BeautifulSoup

# URL сайта, который нужно парсить
url = 'https://example.com'  # Заменить на нужный URL

# Выполняем запрос к сайту
response = requests.get(url)

# Проверяем, успешно ли выполнен запрос
if response.status_code == 200:
    # Парсим HTML-контент
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Здесь мы должны указать, какие данные хотим извлечь
    # Например, извлечем все заголовки h1
    headings = soup.find_all('h1')
    
    # Записываем данные в текстовый файл
    with open('output.txt', 'w', encoding='utf-8') as file:
        for heading in headings:
            file.write(heading.get_text() + '\n')
    
    print('Данные успешно сохранены в output.txt!')
else:
    print(f'Ошибка при запросе: {response.status_code}')
