
import os
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from flask import Flask, render_template, request, redirect, url_for, g, jsonify

app = Flask(__name__)


pool = None

def get_pool():
    global pool
    if pool is None:
        pool = SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD")
        )
    return pool

def get_db_connection():
    if 'db_conn' not in g:
        g.db_conn = get_pool().getconn()
    return g.db_conn

@app.teardown_appcontext
def close_db_connection(e=None):
    db_conn = g.pop('db_conn', None)
    if db_conn is not None:
        get_pool().putconn(db_conn)

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );'''
    )
    conn.commit()
    cur.close()

@app.route('/')
def index():
    create_table()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT content FROM messages ORDER BY created_at DESC;')
    messages = [row[0] for row in cur.fetchall()]
    cur.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    message_content = request.form['new_message'] # Changed from 'content' to 'new_message'
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO messages (content) VALUES (%s)', (message_content,))
    conn.commit()
    cur.close()
    return jsonify({'message': message_content}) # Return JSON for AJAX

@app.route('/clear', methods=['POST'])
def clear():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('TRUNCATE TABLE messages;')
    conn.commit()
    cur.close()
    return jsonify({'status': 'success'}) # Return JSON for AJAX
