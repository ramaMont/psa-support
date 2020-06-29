from flask import Flask
from routes import tickets, clientes
from database import db

app = Flask(__name__)

def create_app():
#	app.config['DEBUG'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	db.init_app(app)
	app.register_blueprint(tickets)
	app.register_blueprint(clientes)
	return app

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_app()
    setup_database(app)
    app.run()
