import requests
import sys

def check_url(url):
    try:
        request = requests.get(url)
        if request.status_code != 200:
            return False

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print e
        sys.exit(1)

def modified_url_format(url_list):
	m_list = [url.replace('/?', '?') for url in url_list]
	return m_list