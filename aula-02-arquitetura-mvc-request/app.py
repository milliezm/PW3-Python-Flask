from flask import Flask, render_template

#importando as rotas que estão nos controllers
from controllers import routes

app = Flask(__name__, template_folder='views')

# chamando as rotas
routes.init_app(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)