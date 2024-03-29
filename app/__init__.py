import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    #configuración de las variables de entorno
    #app.secret_key = 'holamundo'
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
        DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT') 
    )
    from . import db
   
    db.init_app(app) #importar todo el archivo db y ejecutar la funcion init_app 
    
    from . import auth
    from . import todo

    # registro de modulos 
    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    return app