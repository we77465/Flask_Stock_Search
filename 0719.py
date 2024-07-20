import requests
import io
import sys
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():

    originUrl = ["https://news.cnyes.com/news/cat/headline"]
    # 定義要抓取的網址列表
    urls = [
        "https://news.cnyes.com/news/id/5642326",
        "https://news.cnyes.com/news/id/5642325",
        # 添加更多的網址
    ]

    all_news_items = []
    for url in originUrl:
        # 下載網頁內容
        response = requests.get(url)
        html_content = response.content

        # 使用 Beautiful Soup 解析 HTML
        soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")

        # 找到所有 <section style="margin-top:30px"> 元素
        sections = soup.find_all("a", {"style": "margin-top:30px"})

        # 提取每個新聞項目的標題和 URL
        news_items = [] 
        for section in sections:
            content = section.text.strip()
            news_items.append({"content": content})
        all_news_items.extend(news_items)

    # 提取標題 (您可以選擇使用第一個網站的標題,或者自行設定)
    title = soup.title.string

    # 在 Flask 模板中渲染新聞內容
    return render_template("index.html", title=title, news_items=all_news_items)

if __name__ == "__main__":
    app.run(debug=True, port=8000)


# import requests
# import io
# import sys
# from bs4 import BeautifulSoup
# from flask import Flask, render_template, request, redirect, url_for

# # 終端機顯示出中文
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')




# app = Flask(__name__)

# @app.route("/")
# def hello_world(newsContent):
#     return newsContent

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)

# #下載網頁內容
# url = "https://news.cnyes.com/news/id/5642326"
# response = requests.get(url)
# html_content = response.content

# #使用 Beautiful Soup 解析 HTML
# soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")

# #找到所有 <section style="margin-top:30px"> 元素
# sections = soup.find_all("section", {"style": "margin-top:30px"})

# #提取每個新聞項目的標題和 URL
# news_items = []
# for section in sections:
#         content = section.text.strip()
#         news_items.append({"content": content})

# #提取標題
# title = soup.title.string
# print(title)

# hello_world(title)

# print("news_items", news_items)
