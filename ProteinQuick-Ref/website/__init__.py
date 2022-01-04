from flask import Flask,render_template
from os import path

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='HanyangSha'
    
    
    from .searches import searches
    app.register_blueprint(searches,url_prefix='/')
    
    return app