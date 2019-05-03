from flask import Flask, render_template
import requests
import time

app = Flask(__name__)
@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/news")

def news():
    main_url = " https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=cbf1294b5a50472c9145bc11df3932cb "
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    print(results)

    return render_template("news.html", results = results)

@app.route('/live')
def live():
    return render_template('live.html')



if __name__ == '__main__':
    app.run(debug=True)