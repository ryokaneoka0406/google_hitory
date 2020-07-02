import requests


class Crawl(object):
    def _get_html(self, url):
        html = requests.get(url)
        html_text = html.text
        return html_text

    def search_for_word_from_html(self, url, word):
        if word in self._get_html(url):
            return True
        else:
            return False

    def get_urls_with_searchword(self, url_list, word):
        urls_with_keyword = []
        for url in url_list:
            if word in self._get_html(url):
                urls_with_keyword.append(url)

        return urls_with_keyword
