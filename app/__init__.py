from flask import Flask
import secrets 

class MyApp():
    def __init__(self):
        self.app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
        self.app.config['SECRET_KEY'] = secrets.token_hex(16)

        # from .controllers.auth.routes import auth_blueprint
        from .controllers.main.routes import main_blueprint

        # self.app.register_blueprint(auth_blueprint)
        self.app.register_blueprint(main_blueprint)
           
    def run(self):
        self.app.run(debug=True)

