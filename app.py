from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "title": "Главная",
        "welcome_message": "Добро пожаловать в нашу туристическую компанию!",
        "description": "Мы предоставляем лучшие туры и путешествия по всему миру."
    }
    return render_template("home.html", **context)

@app.route("/about")
def about():
    context = {
        "title": "О нас",
        "about_message": "Наша компания занимается организацией путешествий с 2005 года.",
        "services": [
            "Организация туров и путешествий",
            "Бронирование отелей",
            "Экскурсионные программы",
            "Персональные гиды",
            "Сопровождение туристов"
        ]
    }
    return render_template("about.html", **context)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)