from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

from common.fetch_update import insert_urls_to_news_urls
from news_data_creation.news_content_extraction import extract_data_from_url


def get_urls():
    base_url = 'https://www.prnewswire.com/news-releases/automotive-transportation-latest-news/automotive-list/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    # getting response object for the request
    try:
        weburl = base_url
        for i in range(1, 11):
            base_url = '{}?page={}&pagesize=25'.format(base_url, i)
            page = requests.get(base_url, headers=headers, timeout=40)
            soup = BeautifulSoup(page.text, 'html.parser')
            url_lst = soup.find_all('a', class_='newsreleaseconsolidatelink display-outline')

            for j in range(len(url_lst)):
                url = urljoin(base_url, url_lst[j].get('href'))
                # print(url)
                insert_urls_to_news_urls(url, base_url, i)
            base_url = weburl
        extract_data_from_url()

    except Exception as exe:
        print('Exception error occured in get_urls().scraping---%s', exe)


# if __name__ == "__main__":
#     get_urls('https://www.prnewswire.com/news-releases/automotive-transportation-latest-news/automotive-list/')
#     extract_data_from_url()
