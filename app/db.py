import mysql.connector #coneccion con la base de datos mysql
import click #nos permite pasar comandos desde la terminal
from flask import current_app, g #g es una variable dentro de la aplicacion
from flask.cli import with_appcontext #docfunciones
from .schema import instructions # es un archivo

def get_db(): #esta funcion nos conecta a la base de datos y nos devuelve basededatos y el cursor para ejecutar consultas.
    if "db" not in g:
        g.db = mysql.connector.connect(
            # host = current_app.config["DATABASE_HOST"],
            # user = current_app.config["DATABASE_USER"],
            # password = current_app.config["DATABASE_PASSWORD"],
            # database = current_app.config["DATABASE"], 
            # port = current_app.config["DATABASE_PORT"]
            host= "containers-us-west-202.railway.app",
            user= "root",
            password= "QCOxWeyWZirsgzoInoYY",
            database= "railway",
            port= "7891"
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None): #esta funcion permite cerra la db 
    db = g.pop("db",None)

    if db is not None:
        db.close()

def init_db():
    db, c = get_db()
    
    for i in instructions:
        c.execute(i)
    db.commit()

@click.command("init-db")
@with_appcontext

def init_db_command():
    init_db()
    click.echo("base de datos inicializada")



def init_app(app):# esta le permite a la aplicacion cerrar la db una ves terminada una peticion
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
















