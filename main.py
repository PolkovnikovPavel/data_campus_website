from flask import Flask, render_template, redirect, request, abort, url_for
import os


app = Flask(__name__)
#app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=1)
#app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global list_of_products, list_of_products_with_varfarin

    port = int(os.environ.get("PORT", 5000))
    print(1)
    app.run(host='0.0.0.0', port=port)


@app.route("/")
def index():   # главная страница
    data = {}
    data['path_to_bg'] = url_for('static', filename='img/bg.jpg')
    data['path_to_icon'] = url_for('static', filename='img/icon.png')
    return render_template("Main.html", **data)


@app.route("/description")
def description():   # главная страница
    data = {}
    data['path_to_bg'] = url_for('static', filename='img/bg.jpg')
    data['path_to_icon'] = url_for('static', filename='img/icon.png')
    data['path_to_img_1'] = url_for('static', filename='img/screen1.png')

    return render_template("description.html", **data)


@app.route("/work")
def work():   # главная страница
    data = {}
    data['path_to_bg'] = url_for('static', filename='img/bg.jpg')
    data['path_to_icon'] = url_for('static', filename='img/icon.png')
    data['path_to_photo'] = url_for('static', filename='img/photo.jpg')

    return render_template("work.html", **data)


if __name__ == '__main__':
    main()   # старт
