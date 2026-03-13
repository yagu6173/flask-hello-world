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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Creation Successful"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()

    # convert query result to html table by a for loop
    table = "<table>"
    for player in records:
        table += "<tr>"
        for info in player:
            table += "<td>{}</td>".format(info)
        table += "</tr>"
    table += "</table>"     
    return table

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"



