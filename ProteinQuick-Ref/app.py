from flask import Flask, render_template, url_for
from website import create_app
from waitress import serve
if __name__=='__main__':
    app=create_app()
    #app.run()
    serve(app, host='0.0.0.0',port=8000,url_scheme='https')