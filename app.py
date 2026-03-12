# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


import psycopg2

from flask import Flask, url_for, make_response, render_template
app = Flask(__name__)

# internal:
db_url = "postgresql://render_db_ivwe_user:DinCE1inqzLWKKE1K4FBWUf3kcjVsEOD@dpg-d6o265vkijhs73a060s0-a/render_db_ivwe"
# external:
# db_url = "postgresql://render_db_ivwe_user:DinCE1inqzLWKKE1K4FBWUf3kcjVsEOD@dpg-d6o265vkijhs73a060s0-a.oregon-postgres.render.com/render_db_ivwe"


@app.route('/')
def index():
    str = "<h2>Hello World from Yan Gu in 3308 </h2>"
    str += url_for('testing') + '<br>'
    str += url_for('creating') + '<br>'
    str += url_for('inserting') + '<br>'
    str += url_for('selecting') + '<br>'
    str += url_for('dropping')
    return str

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(db_url)
    conn.close()
    return "Database Connection Test Successful"

