import requests
from bs4 import BeautifulSoup
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

def get_html(url):
    # Функция для получения HTML-кода с веб-сайта.

    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при получении HTML: {e}")
        return None
    
def parse(html, page_number):
    # Разбирает заданный HTML-код и извлекает из него информацию.

    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all('div', class_ = 'w-full rounded border')
    data = []

    for items in item:
        item_name = items.find('h4').text.strip()
        price_name = items.find('h5').text.strip()
        item_link = 'https://scrapingclub.com' + items.find('a')['href']
        item_html = get_html(item_link)
        if item_html:
            item_soup = BeautifulSoup(item_html, 'html.parser')
            description = item_soup.find('p', class_ = 'card-description').text.strip()
        else:
            description = 'НЕТ ОПИСАНИЯ'
        data.append((page_number, item_name, price_name, description))

    return data

def create_dataframe(all_data):
    # Функция для создания DataFrame из полученных данных.

    df = pd.DataFrame(all_data, columns=['page_number', 'item_name', 'price_name', 'description'])
    return df

def main(num_pages=1):
    # Основная функция, которая получает данные с веб-сайта и выводит их в виде DataFrame.

    base_url = 'https://scrapingclub.com/exercise/list_basic/?page='
    all_data = []

    for i in range(1, num_pages + 1):
        url = base_url + str(i)
        html = get_html(url)
        if html:
            data = parse(html, i)
            all_data.extend(data)
        else:
            logging.warning("Не удалось получить HTML содержимое страницы")
            continue
    df = create_dataframe(all_data)
    df.to_csv('data.csv', index=False)

    # Визуализация данных.

    plt.figure(figsize=(10, 6))
    df['page_number'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title('Количество товаров на странице')
    plt.xlabel('Номер страницы')
    plt.ylabel('Количество товаров')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--',  alpha=0.7)
    plt.tight_layout()
    plt.show()
 
if __name__ == '__main__':
    main(num_pages=5)