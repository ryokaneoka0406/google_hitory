import unittest

import crawl


class TestCrawl(unittest.TestCase):
    def setUp(self):
        self.crawl = crawl.Crawl()

    def test_get_html(self):
        self.assertIn("Django REST framework", self.crawl._get_html(
            "https://www.django-rest-framework.org/"))

    def test_search_for_word_from_html(self):
        self.assertTrue(
            self.crawl.search_for_word_from_html(
                "https://www.django-rest-framework.org/",
                "Django REST framework"))

    def test_get_urls_with_searchword(self):
        self.assertEqual(
            ["https://www.django-rest-framework.org/",
             "https://docs.djangoproject.com/ja/3.0/"],
            self.crawl.get_urls_with_searchword(
                ["https://www.django-rest-framework.org/",
                 "https://docs.djangoproject.com/ja/3.0/",
                 "http://www.ntv.co.jp/zoo/"],
                "Django"
            )
        )


if __name__ == '__main__':
    unittest.main()
