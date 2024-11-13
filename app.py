from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Контекст для главной страницы
    context = {
        "title": "Главная",
        "welcome_message": "Добро пожаловать в нашу туристическую компанию!",
        "description": "Мы предоставляем лучшие туры и путешествия по всему миру. Планируйте свои поездки с нами и откройте для себя незабываемые места!"
    }
    return render_template("home.html", **context)

@app.route("/about")
def about():
    # Контекст для страницы "О нас"
    context = {
        "title": "О нас",
        "about_message": "Наша компания занимается организацией путешествий с 2005 года. Мы стремимся предоставить нашим клиентам самые уникальные и захватывающие впечатления.",
        "services": [
            "Организация туров и путешествий",
            "Бронирование отелей",
            "Экскурсионные программы",
            "Персональные гиды",
            "Сопровождение туристов"
        ]
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run(debug=True)