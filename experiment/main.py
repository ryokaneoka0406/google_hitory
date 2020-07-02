from crawl import Crawl

crawler = Crawl()

"""
指定のURLの文中にキーワードが含まれるか判定し、
含まれるURLだけ配列に入れて返してくれる
"""

urls = [
    # DjangoとDjango RESTのドキュメントとDjangoについてメモした自分のブログ
    "https://docs.djangoproject.com/ja/3.0/",
    "https://www.django-rest-framework.org/",
    "https://ryopenguin.com/posts/start-django",
    # 世界の果てまで行ってQと笑ってコラえて
    # 当然Djangoとは関係ない
    "https://www.ntv.co.jp/q/",
    "https://www.ntv.co.jp/warakora/"
]

# htmlの文中に「Django」という言葉が含まれるか調べてみる
search_word = "Django"

urls = crawler.get_urls_with_searchword(urls, search_word)
print(urls)
