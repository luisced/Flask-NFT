from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    db = SQLAlchemy()

    # Register blueprints

    from web.users.routes import users

    app.register_blueprint(users)

    return app
