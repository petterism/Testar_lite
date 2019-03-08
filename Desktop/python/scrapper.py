import requests
from bs4 import BeautifulSoup

def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

url = 'http://www.kvartersmenyn.se/norrkoping'
ext = 'index'
result = get_url_paths(url, ext)
print(result)