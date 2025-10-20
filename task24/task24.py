# todo: добавьте во Flask маршруты для страниц (endpoint)
#- О компании
#- Контакты
#- Список постов

from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

menu= {'main' : {'route':'/' , 'title':"Главное меню"},
        'about' : {'route':'/about' , 'title':"О компании"},
        'contacts': {'route':'/contacts' , 'title':"Контакты"},
        'posts' : {'route':'/posts' , 'title':"Список постов"}
        }
@app.route('/')
def index():
    return redirect(url_for('show_page', page='main'))


@app.route('/<page>')
def show_page(page):
    if page in menu:
        return render_template("task24_base.html", title=menu[page]['title'], menu=menu)

if __name__ == "__main__":
    app.run(debug=True)

# Команда для запуска
# flask --app hello run
