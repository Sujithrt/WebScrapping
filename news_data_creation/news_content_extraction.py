from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

from common.fetch_update import fetch_data_from_news_urls, insert_content_to_news_content, update_news_urls_to_P


def extract_data_from_url():
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        # getting response object for the request
        url_lst = fetch_data_from_news_urls()
        for eurl in url_lst:
            # print(eurl['url'])
            update_news_urls_to_P(eurl['id'])
            data = requests.get(eurl['url'], headers=headers, timeout=40)
            soup = BeautifulSoup(data.content, 'html.parser')
            # print(soup.prettify())
            title = soup.find('title').text
            # print(title)
            # author = soup.find('strong', class_='').text
            # print(author)
            published_date = soup.find('p', class_='mb-no').text[0:6]
            # print(published_date)
            published_year = soup.find('p', class_='mb-no').text[8:12]
            # print(published_year)
            # description = soup.find('div', class_='row').text
            # print(description)
            # description = ''
            # desc = soup.find_all('p')
            # for ele in desc:
            #     description = description + ele.text + "\n"
            insert_content_to_news_content(eurl['id'], title, published_date, published_year)

    except Exception as exe:
        print("Exception in extract_data_from_url", exe)


# extract_data_from_url()
